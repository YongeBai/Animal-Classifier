### Animal classifier using YOLOv5

This project uses the YOLOv5 object detection model to detect animals in an image. The project provides a simple Flask app that allows the user to upload an image and see the detected animals in it.

## Requirements
- Flask
- PyTorch
- OpenCV

## Usage
To run the app, use the following command:
```
python main.py
```
This will start a Flask web server at the address http://0.0.0.0:5000/. You can then open this address in a web browser and use the app to upload an image and detect animals in it. The app will display the predicted class name and a flag indicating whether the detected object is an animal or not.

## Configuration
The app has several parameters that can be modified to change its behavior:

- `file_path`: This is the path where the uploaded images will be saved. You can change this to a different location if needed.
- `model.conf`: This is the minimum confidence level for detecting objects. Objects with a lower confidence will not be displayed.
- `model.iou`: This is the minimum IoU threshold for detecting objects. Objects with a lower IoU will not be displayed.

## Limitations
The accuracy of the animal detection depends on the quality of the input image and the lighting conditions. In low light or noisy environments, the detection may not work as well. The app also assumes that the animal classes are located between 14 and 23 in the list of classes provided by the YOLOv5 model. This may not be the case for all models or datasets.
