# 🎨 Real-Time Multi-Color Object Detection using OpenCV (v1.2)

A real-time computer vision application built with **Python** and **OpenCV** for detecting and tracking multiple colored objects through webcam input.

This project started as a basic single-color tracking exercise and was gradually improved into a modular computer vision system with multiple detection, visualization, recording, and camera control features.

---

## 🚀 Features

### 🎯 Object Detection

- Real-time webcam based detection
- Multiple color detection using HSV color space
- Contour-based object detection
- Noise reduction using Morphological Operations
- Object filtering based on area threshold


---

### 🎨 Detection Visualization

- Color-specific bounding boxes
- Object name display
- Object area calculation (pixels)
- Object center point marker
- Improved YOLO-style label background
- Total detected object counter


---

### 🎥 Camera & Media Features

- FPS monitoring
- Screenshot capture
- Video recording
- Recording status indicator
- Multiple camera switching support


---

## 🎮 Controls

| Key | Action |
|---|---|
| `Q` | Quit Application |
| `S` | Capture Screenshot |
| `R` | Start / Stop Video Recording |
| `C` | Switch Camera |


---

# 🧠 Computer Vision Concepts Used

This project demonstrates:

- Image Processing Pipeline
- BGR to HSV Conversion
- HSV Color Segmentation
- Color Thresholding
- Binary Mask Creation
- Morphological Opening
- Morphological Closing
- Contour Detection
- Bounding Box Calculation
- Real-time Frame Processing


---

# 🛠 Technologies Used

- Python
- OpenCV
- NumPy


---

# 📂 Project Structure

```
Real-Time-Multi-Color-Object-Detection/

│
├── main.py
│
├── detector.py
│
├── colors.py
│
├── utils.py
│
├── requirements.txt
│
├── README.md
│
└── outputs/

    ├── screenshots/

    └── videos/
```

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Arnabtheaich/Real-Time-Multi-Color-Object-Detection.git
```

Go to project folder:

```bash
cd Real-Time-Multi-Color-Object-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

# 🌈 Supported Colors

Current supported colors:

- 🟡 Yellow
- 🔵 Blue
- 🟢 Green
- 🟠 Orange
- 🟣 Purple
- 🔴 Red

> Black and White detection are currently disabled to reduce false detection caused by shadows and lighting variations.


---

# 📸 Output

Example detection includes:

```
Detected Color

↓

Bounding Box

↓

Object Area

↓

Center Point
```


<p align="center">
  <img src="outputs\videos\recording_5.gif" alt="preview" width="100%">
</p>

---

# 📌 Version History


## v1.0

Initial learning version:

- Single color detection
- Basic HSV masking
- Basic bounding box tracking


---

## v1.1

Major refactoring:

Added:

- Multi-color detection
- Modular code structure
- Contour based detection
- FPS counter
- Screenshot capture
- Object counting
- Noise filtering


---

## v1.2 (Current)

Application improvement update:

Added:

- Color-wise bounding boxes
- Object area display
- Improved detection labels
- Video recording feature
- Recording indicator
- Camera switching
- Better project structure


---

# 🔮 Future Improvements

Planned features:

- 🎛️ HSV Trackbars
- 🖱️ Mouse based HSV picker
- 🔺 Shape Detection
- ⭕ Circle Detection
- 📏 Distance Estimation
- 🎥 Video file processing
- 🌐 Streamlit Web Application
- 🤖 YOLO integration


---

# 📚 Learning Purpose

This project was developed step-by-step while learning Computer Vision.

The goal was not only to build a working detector, but also to understand how real-time image processing systems work internally.

Main learning areas:

- Writing modular Python code
- Understanding OpenCV workflow
- Improving detection accuracy
- Building scalable project architecture


---

# 👨‍💻 Author

**Arnab Aich**

- GitHub: https://github.com/Arnabtheaich
- LinkedIn: https://www.linkedin.com/in/arnab-aich/


---

⭐ If you find this project helpful, consider giving it a star!