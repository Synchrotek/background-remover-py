import time, io, numpy as np
from cv2 import MORPH_ELLIPSE, getStructuringElement 
from PIL import Image
from PIL.Image import Image as PILImage
from typing import List, Union
from enum import Enum
from utils import new_session


start_time = time.time()
kernel = getStructuringElement(MORPH_ELLIPSE, (3, 3))

def main():
    # input_path = 'anya02.webp'
    input_path = 'input.jpg'
    output_path = 'output.png'

    img = Image.open(input_path)
    output = remove(img)
    output.save(output_path)

class ReturnType(Enum):
    BYTES = 0
    PILLOW = 1
    NDARRAY = 2

def naive_cutout(img: PILImage, mask: PILImage) -> PILImage:
    empty = Image.new("RGBA", (img.size), 0)
    cutout = Image.composite(img, empty, mask)
    return cutout

def get_concat_v_multi(imgs: List[PILImage]) -> PILImage:
    pivot = imgs.pop(0)
    for im in imgs:
        pivot = get_concat_v(pivot, im)
    return pivot


def get_concat_v(img1: PILImage, img2: PILImage) -> PILImage:
    dst = Image.new("RGBA", (img1.width, img1.height + img2.height))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (0, img1.height))
    return dst


def remove(data: Union[bytes, PILImage, np.ndarray]
           ) -> Union[bytes, PILImage, np.ndarray]:
    if isinstance(data, PILImage):
        return_type = ReturnType.PILLOW
        img = data
    elif isinstance(data, bytes):
        return_type = ReturnType.BYTES
        img = Image.open(io.BytesIO(data))
    elif isinstance(data, np.ndarray):
        return_type = ReturnType.NDARRAY
        img = Image.fromarray(data)
    else:
        raise ValueError("Input type {} is not supported.".format(type(data)))

    session = new_session("u2net")

    masks = session.predict(img)
    # print(masks)
    cutouts = []

    for mask in masks:
        cutout = naive_cutout(img, mask)
        cutouts.append(cutout)

    cutout = img
    if len(cutouts) > 0:
        # print("len(cutouts) > 0 : true")
        cutout = get_concat_v_multi(cutouts)

    if ReturnType.PILLOW == return_type:
        end_time = time.time()
        execution_time = end_time - start_time
        # print("Execution time: {:.3f} seconds".format(execution_time))
        return cutout

    if ReturnType.NDARRAY == return_type:
        return np.asarray(cutout)

    bio = io.BytesIO()
    cutout.save(bio, "PNG")
    bio.seek(0)

    return bio.read()

if __name__ == "__main__":
    main()
