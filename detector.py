import torch
import cv2 as cv
import numpy as np
import os

class AnimalCLassifier:
    def __init__(self) -> None:

        self.animals = []

        self.model = torch.hub.load(
            'ultralytics/yolov5', 
            'yolov5s', 
            pretrained=True,
            verbose=False)
        self.model.conf = 0.25  # NMS confidence threshold
        self.model.iou = 0.45 # IoU threshold
        self.classes = self.model.names
        self.model.multi_label = False 
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def label_to_class(self, label):
        return self.classes[(int(label))]

    def isAnimal(self, label):
        if 14 <= label <= 23:
            return True
        else:
            return False


    def detect(self, folder, input_image):
        img_bgr = cv.imread((os.path.join(folder,input_image)))
        img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
        results = self.model(img_rgb)
        label = results.xyxyn[0][:, -1]
        prediction = self.label_to_class(label)
        animal = self.isAnimal(label)
        
        return (prediction, animal)

# detector = AnimalCLassifier()
# print(detector.detect("cat.png"))
