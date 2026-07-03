import cv2

from colors import COLOR_RANGES
from utils import draw_label, draw_center


def detect_objects(frame, hsv_frame, min_area=1000):
    """
    Detect colored objects using HSV segmentation
    and contour detection.
    """

    detections = []


    # Loop through every color
    for color_name, values in COLOR_RANGES.items():


        # Get color information
        lower = values["lower"]
        upper = values["upper"]
        draw_color = values["draw_color"]


        # Create binary mask
        mask = cv2.inRange(
            hsv_frame,
            lower,
            upper
        )


        # Noise removal kernel
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (3, 3)
        )


        # Remove small white noise
        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel
        )


        # Fill small black holes
        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            kernel
        )


        # Find separate objects
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )


        # Process every object
        for contour in contours:


            area = cv2.contourArea(contour)


            # Ignore small objects/noise
            if area < min_area:
                continue


            # Bounding box
            x, y, w, h = cv2.boundingRect(
                contour
            )


            # Object center
            center_x = x + w // 2
            center_y = y + h // 2



            # ----------------------------
            # Draw Color Based Rectangle
            # ----------------------------

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                draw_color,
                2
            )



            # ----------------------------
            # Draw Center Point
            # ----------------------------

            draw_center(
                frame,
                center_x,
                center_y
            )



            # ----------------------------
            # Display Label + Area
            # ----------------------------

            label = f"{color_name} | {int(area)} px"


            draw_label(
                frame,
                label,
                x,
                y - 10
            )



            # Store detection data
            detections.append(
                {

                    "color": color_name,

                    "area": int(area),

                    "center": (
                        center_x,
                        center_y
                    ),

                    "bbox": (
                        x,
                        y,
                        w,
                        h
                    )

                }
            )


    return frame, detections