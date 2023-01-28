<h1 align="center"><strong>background-remover-python3</strong></h1>
<p><h2 align="center">In this repository The "bg-remove.py" file receives an image as input and process it to remove it's Background</h2></p>

<details close> 
  <summary><h2>Demo 1 (click)</h2></summary>
  <table>
    <tr>
    <th>
    <img alt="Demo-image-1" src="https://user-images.githubusercontent.com/77431114/215275187-4ef372f8-4fe6-4035-adc2-c606f2409584.png"/></th>
    </tr>
  </table>
</details>

<details open> 
  <summary><h2>Demo 2 (click)</h2></summary>
  <table>
    <tr>
      <th>Running the "bg-remove.py" file receives an image whose path is defined in variable "input_path"
      which removes background and saves it in "output.png" as shown below</th>
    </tr>
    <tr>
    <th>
    <img alt="Demo-image-1" src="https://user-images.githubusercontent.com/77431114/215275192-77287d58-1b59-4737-b1df-9c1e0fd5be0d.png"/></th>
    </tr>
  </table>
</details>

Requirements
============
* Linux or macOS or Windows
* [ Python 3 ](https://www.python.org/downloads/)Interpreter
* [ Pillow ](https://pypi.org/project/Pillow/)Library
* [ typing ](https://pypi.org/project/typing/)Library
* [ opencv ](https://pypi.org/project/opencv-python/)Library
* [ onnxruntime ](https://pypi.org/project/onnxruntime/)Library
* [ numpy ](https://pypi.org/project/numpy/)Library
* <details open> 
  <summary><span><a href="https://mega.nz/file/wV5zECYb#C19BLp57nJ8b_7LVZDajWLDRf5HSml63n0skiK2bNuQ">u2net.onnx</a> pretrained model</span></summary>
  <table>
<ul>
    <li>As This Project uses a pretrained ML model File This is needed to run the "bg-remove.py" </li>
    <li>You can Get that File <a href="https://mega.nz/file/wV5zECYb#C19BLp57nJ8b_7LVZDajWLDRf5HSml63n0skiK2bNuQ">HERE</a></li>
    <li>After Downloading it, just Put it in the same directory as "bg-remove.py"</a></li>
</ul>
  </table>
</details>



<br>

Setup
============
* Download the [ Project files ](https://github.com/PuL5TaR/ascii-art-generator-python3/archive/refs/heads/main.zip)
* Extract the downloaded zip file
* go to the extracted directory

<br>

How to use
============
After setup go to the base directory of remove-bg.py

run that python file through terminal in that directory
```
 python remove-bg.py
```
To input a specific image file 
* open remove-bg.py in any text-editor and
* Inside "main()" method give the relative or full path of Image to "input_path" Variable 
* The Images like ( .png, .jpg. jpeg .webp etc ) are all allowed

for example : `input_path = 'Images/myCustomImage.png'`

After running the "main.py" you will get the output Image in the same directory in "output.png"

<br>
<hr>
