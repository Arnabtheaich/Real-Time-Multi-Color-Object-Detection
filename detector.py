import cv2

from colors import COLOR_RANGES
from utils import draw_label, draw_center


def detect_objects(frame, hsv_frame, min_area=1000):
    """
    Detect multiple colored objects from an HSV image.

    Parameters
    ----------
    frame : Original BGR Frame
    hsv_frame : HSV converted frame
    min_area : Ignore very small objects (noise)

    Returns
    -------
    frame : Frame with drawings
    detections : List of detected objects
    """

    detections = []

    # Loop through every color
    for color_name, (lower, upper) in COLOR_RANGES.items():

        # Create binary mask
        mask = cv2.inRange(hsv_frame, lower, upper)

        # Remove Noise
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (5, 5)
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            kernel
        )

        # Find contours
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Loop through every detected contour
        for contour in contours:

            area = cv2.contourArea(contour)

            if area < min_area:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            center_x = x + w // 2
            center_y = y + h // 2

            # Draw Rectangle
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Draw Center
            draw_center(
                frame,
                center_x,
                center_y
            )

            # Draw Label
            draw_label(
                frame,
                f"{color_name}",
                x,
                y - 10
            )

            detections.append({

                "color": color_name,

                "area": area,

                "center": (center_x, center_y),

                "bbox": (x, y, w, h)

            })

    return frame, detections