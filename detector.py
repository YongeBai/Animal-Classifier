import torch
import cv2 as cv
import numpy as np
import os

class AnimalCLassifier:
    def __init__(self) -> None:
        # initialize empty list to store detected animals
        self.animals = []

        # load pre-trained YOLOv5 model from PyTorch Hub
        self.model = torch.hub.load(
            'ultralytics/yolov5', 
            'yolov5s', 
            pretrained=True,
            verbose=False)

        # set model confidence and IoU thresholds
        self.model.conf = 0.25
        self.model.iou = 0.45

        # get class names from the model
        self.classes = self.model.names

        # set multi-label flag to False
        self.model.multi_label = False 

        # set device to use GPU if available, else use CPU
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def label_to_class(self, label):
        # return class name corresponding to the given label
        return self.classes[(int(label))]

    def isAnimal(self, label):
        # check if the label corresponds to an animal class
        if 14 <= label <= 23:
            return True
        else:
            return False

    def detect(self, folder, input_image):
        # read input image from the given folder
        img_bgr = cv.imread((os.path.join(folder,input_image)))

        # convert image to RGB color space
        img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)

        # detect objects in the image using the YOLOv5 model
        results = self.model(img_rgb)

        # get label of the detected object
        label = results.xyxyn[0][:, -1]

        # get class name corresponding to the detected object's label
        prediction = self.label_to_class(label)

        # check if the detected object is an animal
        animal = self.isAnimal(label)
        
        # return tuple with class name and animal flag
        return (prediction, animal)

# create an instance of the AnimalClassifier
# detector = AnimalCLassifier()

# detect animals in an image
# print(detector.detect("cat.png"))


