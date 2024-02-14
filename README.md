<h1 align="center">
  <br>
   Image Labeling and Colorization Script
  <br>
</h1>

<h4 align="center">This repository contains a Python script that performs image labeling and colorization on binary images using a two-pass labeling algorithm.
  
<p align="center">
  <a href="https://"><img src="https://img.shields.io/badge/language-Python-2ea42f?logo=python" alt="language - Python"></a>
  <a href="https://"><img src="https://img.shields.io/badge/OpenCV application-localhost-orange?logo=IDE" alt="OpenCV application"></a>
  <br>
</p>


# Description

## Overview

The script reads a binary image, performs two-pass labeling to identify connected components, assigns unique labels to each connected component, and colorizes the labeled regions. The resulting colorized image is then displayed and saved.

## Features

- **Binarization**: Converts the input image into a binary image using a specified threshold.
- **Two-Pass Labeling**: Identifies connected components in the binary image using a two-pass labeling algorithm.
- **Colorization**: Assigns random colors to each labeled region in the image to differentiate between different connected components.
- **Visualization**: Displays the colorized image and saves it to a file.

## Usage

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Place the input images in the `input_images` directory.
3. Run the script `Run_two_pass.py`.
4. The colorized image will be displayed, and the output will be saved in the `output_images` directory as `Output_Colorized_Image.jpg`.

### Before
![Input_not_Colorized_Image](https://github.com/ChanvithaPraveen/Connected-Components-Two-Pass-Algorithm/assets/78690169/fc9ca91a-8ee4-450c-bb7e-b9ef07149e3c)
### After
![Output_Colorized_Image](https://github.com/ChanvithaPraveen/Connected-Components-Two-Pass-Algorithm/assets/78690169/6bfeb9f1-2bc2-42c2-9d9a-81fe0d3f234b)

