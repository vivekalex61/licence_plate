
#!pip install opencv-python
#!pip install pytesseract
#sudo apt update
#sudo apt install tesseract-ocr
#sudo apt install libtesseract-dev
import pytesseract
import numpy as np
import cv2

import sys

if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('You need to specify the path to be listed')
    sys.exit()

path=sys.argv[1]
image = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
#im_bw = cv2.threshold(adjusted, 180, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((1, 1), np.uint8)
'''
 image processing operations are applied to grayscale or binary images and are used for preprocessing for OCR algorithms, detecting barcodes, detecting license plates, and more.We can use morphological operations to increase the size of objects in images as well as decrease them. We can also utilize morphological operations to close gaps between objects as well as open them.
ref: https://pyimagesearch.com/2021/04/28/opencv-morphological-operations/
'''
opening = cv2.morphologyEx(
image, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
gray = cv2.medianBlur(closing, 3)
'''
Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.
'''
text = pytesseract.image_to_string(gray)
print(f"Detected Number {text}")

