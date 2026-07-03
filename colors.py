import numpy as np

# HSV Color Ranges
# Format:
# "Color Name": (Lower HSV, Upper HSV)

COLOR_RANGES = {

    "Yellow": (
        np.array([20, 100, 100]),
        np.array([35, 255, 255])
    ),

    "red": (
        np.array([0, 100, 100]),
        np.array([10, 255, 255])
    ),

    "Blue": (
        np.array([100, 100, 100]),
        np.array([130, 255, 255])
    ),

    "Green": (
        np.array([40, 70, 70]),
        np.array([80, 255, 255])
    ),

    "Orange": (
        np.array([10, 120, 120]),
        np.array([20, 255, 255])
    ),

    "Purple": (
        np.array([130, 80, 80]),
        np.array([160, 255, 255])
    ),

    "White": (
        np.array([0, 0, 180]),
        np.array([180, 60, 255])
    ),

    "Black": (
        np.array([0, 0, 0]),
        np.array([180, 255, 40])
    )

}