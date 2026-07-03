import numpy as np


COLOR_RANGES = {


    "Red": {

    "lower": np.array([0, 150, 120]),
    "upper": np.array([10, 255, 255]),

    "draw_color": (0,0,255)

    },


    "Orange": {

        "lower": np.array([11, 100, 100]),
        "upper": np.array([25, 255, 255]),

        "draw_color": (0, 165, 255)

    },


    "Yellow": {

        "lower": np.array([20, 100, 100]),
        "upper": np.array([35, 255, 255]),

        # BGR color for OpenCV drawing
        "draw_color": (0, 255, 255)

    },


    "Green": {

        "lower": np.array([36, 50, 50]),
        "upper": np.array([85, 255, 255]),

        "draw_color": (0, 255, 0)

    },


    "Blue": {

        "lower": np.array([90, 70, 50]),
        "upper": np.array([130, 255, 255]),

        "draw_color": (255, 0, 0)

    },


    "Purple": {

        "lower": np.array([130, 50, 50]),
        "upper": np.array([160, 255, 255]),

        "draw_color": (255, 0, 255)

    }

}