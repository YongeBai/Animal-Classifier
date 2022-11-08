import torch
import cv2 as cv
import numpy as np

class AnimalCLassifier:
    def __init__(self) -> None:
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
        print("Device: ", self.device)


    def detect(self, input_image):
        img_bgr = cv.imread(input_image)
        img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
        results = self.model(img_rgb)
        results.show()


detector = AnimalCLassifier()
detector.detect("cat.png")