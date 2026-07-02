import cv2
import time


# -----------------------------
# FPS Counter
# -----------------------------
class FPS:

    def __init__(self):
        self.prev_time = time.time()

    def update(self):
        current_time = time.time()

        fps = 1 / (current_time - self.prev_time)

        self.prev_time = current_time

        return int(fps)


# -----------------------------
# Draw Label
# -----------------------------
def draw_label(frame, text, x, y):

    cv2.putText(
        frame,
        text,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


# -----------------------------
# Draw Center Point
# -----------------------------
def draw_center(frame, x, y):

    cv2.circle(
        frame,
        (x, y),
        5,
        (0, 0, 255),
        -1
    )


# -----------------------------
# Save Screenshot
# -----------------------------
def save_frame(frame, filename):

    cv2.imwrite(filename, frame)