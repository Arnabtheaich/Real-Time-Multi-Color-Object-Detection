# Real-Time Single Color Detection using OpenCV

A beginner computer vision project built with Python and OpenCV that detects a single color (yellow) in real time using HSV color segmentation.

> This project was created while learning OpenCV by following an online tutorial. It helped me understand the fundamentals of real-time color detection, HSV color space, masking, and bounding boxes.

## Features

- Real-time webcam capture
- HSV color space conversion
- Single color (yellow) detection
- Bounding box around detected object
- Press `Q` to quit

## Technologies

- Python
- OpenCV
- NumPy
- Pillow

## Learning Outcomes

Through this project I learned:

- How OpenCV captures webcam frames
- BGR vs HSV color spaces
- HSV thresholding using `cv2.inRange()`
- Binary masks
- Bounding box detection
- Basic real-time computer vision pipeline

## Future Improvements

A more advanced version of this project includes:

- Multiple color detection
- Contour-based detection
- FPS counter
- Noise removal
- Screenshot capture
- Shape detection

## Run

```bash
pip install -r requirements.txt
python main.py
```
