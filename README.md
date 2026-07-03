# 🎨 Real-Time Multi-Color Object Detection (v1.1)

A real-time computer vision project built with **Python** and **OpenCV** that detects multiple colored objects using HSV color segmentation. This project was developed as an improved version of my initial single-color detection project and focuses on writing cleaner, modular, and more scalable OpenCV code.

---

## ✨ Features

- 🎥 Real-time webcam detection
- 🌈 Multi-color object detection
- 🟨 Supports:
  - Yellow
  - Blue
  - Green
  - Orange
  - Purple
  - White
  - Black
- 📦 Contour-based object detection
- 🟩 Bounding boxes around detected objects
- 📍 Object center point visualization
- ⚡ Real-time FPS counter
- 📊 Total detected object counter
- 🖼️ Screenshot capture (`S` key)
- ❌ Exit application (`Q` key)
- 🧹 Noise reduction using Morphological Operations
- 🧩 Modular project architecture

---

## 🧠 Computer Vision Concepts Used

- OpenCV
- HSV Color Space
- Color Thresholding
- Binary Masking
- Contour Detection
- Bounding Rectangle
- Morphological Opening & Closing
- Image Processing Pipeline
- Real-Time Video Processing

---

## 📂 Project Structure

```
Real-Time-Multi-Color-Object-Detection/

│── main.py
│── detector.py
│── colors.py
│── utils.py
│── requirements.txt
│── README.md

├── outputs/
│   └── screenshots/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Arnabtheaich/Real-Time-Multi-Color-Object-Detection.git
```

Move into the project

```bash
cd Real-Time-Multi-Color-Object-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| **S** | Save Screenshot |
| **Q** | Quit |

---

## 📦 Dependencies

- Python 3.x
- OpenCV
- NumPy

Install

```bash
pip install -r requirements.txt
```

---

## 📸 Sample Output

<p align="center">
  <img src="E:\VS CODE\Color-Detection-project-OpenCV\assets\demo.png" alt="Dashboard Demo" width="100%">
</p>

---

## 🔄 Version History

### v1.0
- Single color tracking (tutorial implementation)

### v1.1 (Current)
- Complete project refactoring
- Modular architecture
- Multi-color detection
- Contour-based object detection
- FPS counter
- Object counter
- Screenshot functionality
- Morphological noise removal

---

## 🚀 Planned Features

- 🎥 Video Recording
- 🎛️ HSV Trackbars
- 🔺 Shape Detection
- ⭕ Circle Detection
- 📏 Object Area Display
- 🎨 Color-wise Bounding Boxes
- 📈 Performance Improvements

---

## 📖 Learning Note

This project began as a simple single-color tracking exercise while learning OpenCV. Instead of keeping it as a tutorial implementation, I gradually redesigned and extended it into a modular multi-color object detection system by applying additional computer vision concepts and improving the project architecture.

---

## 👨‍💻 Author

**Arnab Aich**

- GitHub: https://github.com/Arnabtheaich
- LinkedIn: *(Add your LinkedIn profile here)*

---

⭐ If you found this project interesting, consider giving it a star.
