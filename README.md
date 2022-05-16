
# Number Plate identifier  

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

Script for detecting a numberplate of vehicles and list the numbers on it to chechk wherther the vehicle is clean or not.



## Introduction 

#### Why Number plate identification?

Recognizing Car License Plate is a very important task for a camera surveillance-based security system. Most of the culprits uses stolen vehicles for crimes and escaped using those vehicles. It will be very useful if we can identify the vehice position early as possible. 
Number plate detector helps to identify numberplates of each vehicle and decode it's number.
We can extract the license plate from an image using some computer vision techniques and then we can use Optical Character Recognition to recognize the license number.

## Overview 
- Datasets and Data-Loading
- Image Preprocessing
- Model creation

### Datasets and Data-Loading

Dataset was collected from https://dataturks.com/projects/devika.mishra/Indian_Number_plates . Contains the images of the cars, number plates and annotations in .txt files (YOLO format)

### image Preprocessing

The aim of pre-processing is an improvement of the image data that suppresses undesired distortions or enhances some image features relevant for further processing and analysis task.
. The aim of pre-processing is an improvement of the image data that suppresses undesired distortions or enhances some image features relevant for further processing and analysis task. 
 For yolov5 we just scaled each image into 640*480 

Ref : https://www.mygreatlearning.com/blog/introduction-to-image-pre-processing/
 

### image Annotation
Most annotation platforms support export at YOLO labeling format, providing one annotations text file per image. Each text file contains one bounding-box (BBox) annotation for each of the objects in the image. The annotations are normalized to the image size, and lie within the range of 0 to 1. They are represented in the following format:
< object-class-ID> <X center> <Y center> <Box width> <Box height>
### Model building and training

Model building has two parts:

1)Number Plate Detection. This problem can be tackled using the Object Detection approach where we need to train our model using the car/other vehicle images with number plates.

2)Extracting text from the detected Number Plate. This problem can be solved using OCR(Optical Character Recognition) which can be helpful in extracting alphanumeric characters from cropped Number Plate images.


#### 1)Number Plate Detection :
We are using YOLOV5 for numberplate detection. YOLOv5 rocket is a family of object detection architectures and models pretrained on the COCO dataset, and represents Ultralytics open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.
Since our dataset is relatively small (~250 images), transfer learning is expected to produce better results than training from scratch. 
ref: https://github.com/ultralytics/yolov5



#### 1)Extracting text from the detected Number Plate:
Googles tesseract is used for extracting values from numberplate. Tesseract is an open source optical character recognition (OCR) platform. OCR extracts text from images and documents without a text layer and outputs the document into a new searchable text file, PDF, or most other popular formats.

ref : https://github.com/tesseract-ocr/tesseract

## Predictions

### to make prediction run below codes


1) `Download yolov5 model from drive( https://drive.google.com/file/d/1NoemFWlmVYUmLLDWeIyY5Af_MpoIEgY1/view?usp=sharing ) to the pulled directory `

2) `Unzip yolo5.zip to get trained models`

3) `python3 yolov5/train.py --img 640 --batch 16 --epochs 300 --data yolov5/data.yaml --weights yolov5s.pt`

3) `python3 detect_number.py path_to_detected_numberplates`


Detected number plate :

![alt text](https://raw.githubusercontent.com/vivekalex61/licence_plate/main/images/car10_full.jpg)   ![alt text](https://raw.githubusercontent.com/vivekalex61/licence_plate/main/images/car0_full.jpg)


Croped number plate:

![alt text](https://raw.githubusercontent.com/vivekalex61/licence_plate/main/images/car10.jpg) 

![alt text](https://raw.githubusercontent.com/vivekalex61/licence_plate/main/images/car0.jpg) 

Extracted number:

![alt text](https://raw.githubusercontent.com/vivekalex61/licence_plate/main/images/detect1.png) 

![alt text](https://raw.githubusercontent.com/vivekalex61/licence_plate/main/images/detect2.png) 

## End Notes

The model is not finetuned .
