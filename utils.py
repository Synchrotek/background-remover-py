import os, numpy as np
from typing import Dict, List, Tuple
import onnxruntime as ort
from PIL import Image
from PIL.Image import Image as PILImage

class SimpleSession():
    def __init__(self, model_name: str, inner_session: ort.InferenceSession):
        self.model_name = model_name
        self.inner_session = inner_session
        
    def normalize(
        self,
        img: PILImage,
        mean: Tuple[float, float, float],
        std: Tuple[float, float, float],
        size: Tuple[int, int],
    ) -> Dict[str, np.ndarray]:
        im = img.convert("RGB").resize(size, Image.LANCZOS)
     
        im_ary = np.array(im)
        im_ary = im_ary / np.max(im_ary)

        tmpImg = np.zeros((im_ary.shape[0], im_ary.shape[1], 3))
        tmpImg[:, :, 0] = (im_ary[:, :, 0] - mean[0]) / std[0]
        tmpImg[:, :, 1] = (im_ary[:, :, 1] - mean[1]) / std[1]
        tmpImg[:, :, 2] = (im_ary[:, :, 2] - mean[2]) / std[2]

        tmpImg = tmpImg.transpose((2, 0, 1))

        return {
            self.inner_session.get_inputs()[0]
            .name: np.expand_dims(tmpImg, 0)
            .astype(np.float32)
        }

    def predict(self, img: PILImage) -> List[PILImage]:
        ort_outs = self.inner_session.run(
            None,
            self.normalize(
                img, (0.485, 0.456, 0.406), (0.229, 0.224, 0.225), (320, 320)
            ),
        )
        pred = ort_outs[0][:, 0, :, :]

        ma = np.max(pred)
        mi = np.min(pred)

        pred = (pred - mi) / (ma - mi)
        pred = np.squeeze(pred)

        mask = Image.fromarray((pred * 255).astype("uint8"), mode="L")
        mask = mask.resize(img.size, Image.LANCZOS)

        return [mask]


def new_session(model_name: str = "u2net"):
    session_class = SimpleSession
    
    full_path = 'u2net.onnx'
    sess_opts = ort.SessionOptions()

    # if use more Threads for ONNX model during inference then
    # make sess_opts.inter_op_num_threads = NoOfThread
    if "OMP_NUM_THREADS" in os.environ:
        sess_opts.inter_op_num_threads = int(os.environ["OMP_NUM_THREADS"])

    return session_class(
        model_name,
        ort.InferenceSession(
            str(full_path),
            sess_options=sess_opts,
            # providers=ort.get_available_providers(),
        ),
    )
