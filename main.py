import cv2
import os

from detector import detect_objects
from utils import FPS, draw_label, save_frame


# -----------------------------
# Create Output Folder
# -----------------------------
os.makedirs("outputs/screenshots", exist_ok=True)


# -----------------------------
# Initialize Camera
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


# -----------------------------
# FPS Counter
# -----------------------------
fps_counter = FPS()

image_number = 1


# -----------------------------
# Main Loop
# -----------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR -> HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect Objects
    frame, detections = detect_objects(
        frame,
        hsv_frame
    )

    # FPS
    fps = fps_counter.update()

    draw_label(
        frame,
        f"FPS : {fps}",
        10,
        30
    )

    # Number of Objects
    draw_label(
        frame,
        f"Objects : {len(detections)}",
        10,
        60
    )

    # Controls
    draw_label(
        frame,
        "Q : Quit",
        10,
        90
    )

    draw_label(
        frame,
        "S : Screenshot",
        10,
        120
    )

    cv2.imshow(
        "Real-Time Multi Color Detection",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    # Quit
    if key == ord("q"):
        break

    # Screenshot
    elif key == ord("s"):

        filename = f"outputs/screenshots/frame_{image_number}.jpg"

        save_frame(frame, filename)

        print(f"Saved : {filename}")

        image_number += 1


# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()