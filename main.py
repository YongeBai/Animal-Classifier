

import torch
import cv2 as cv
import numpy as np

class AnimalCLassifier:
    def __init__(self) -> None:
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', verbose=False)


    def __call__(self):
        img = cv.imread("cat.png")
        results = self.model(img)
        results.show()


detect = AnimalCLassifier()
detect()
detect.model