import cv2
import time


# ============================================================
# FPS COUNTER CLASS
# ============================================================

class FPS:
    """
    Calculate Frames Per Second (FPS)
    for real-time video processing.
    """

    def __init__(self):

        # Store initial time
        self.prev_time = time.time()


    def update(self):

        # Current frame time
        current_time = time.time()


        # FPS = 1 / time difference between frames
        fps = 1 / (current_time - self.prev_time)


        # Update previous time
        self.prev_time = current_time


        return int(fps)



# ============================================================
# DRAW TEXT LABEL WITH BACKGROUND
# ============================================================

def draw_label(
        frame,
        text,
        x,
        y,
        color=(0, 255, 0)
):

    """
    Draw text with a filled background box.

    Similar style to modern object detection models
    like YOLO.

    Parameters:
        frame : image/frame
        text  : label text
        x,y   : position
        color : background color
    """


    font = cv2.FONT_HERSHEY_SIMPLEX

    font_scale = 0.6

    thickness = 2


    # Get text width and height
    text_size, _ = cv2.getTextSize(
        text,
        font,
        font_scale,
        thickness
    )


    text_width, text_height = text_size



    # Draw filled rectangle behind text
    cv2.rectangle(
        frame,

        (x, y - text_height - 10),

        (x + text_width, y),

        color,

        -1
    )



    # Draw actual text
    cv2.putText(
        frame,

        text,

        (x, y - 5),

        font,

        font_scale,

        (255, 255, 255),

        thickness
    )




# ============================================================
# DRAW OBJECT CENTER POINT
# ============================================================

def draw_center(
        frame,
        x,
        y
):

    """
    Draw a small circle at the center
    of detected object.
    """


    cv2.circle(

        frame,

        (x, y),

        5,

        (0, 0, 255),

        -1
    )





# ============================================================
# SAVE SCREENSHOT
# ============================================================

def save_frame(
        frame,
        filename
):

    """
    Save current frame as an image.
    """


    cv2.imwrite(
        filename,
        frame
    )





# ============================================================
# VIDEO RECORDER CLASS
# ============================================================

class VideoRecorder:


    """
    Handles video recording.

    Features:
    - Start recording
    - Stop recording
    - Save output video
    """



    def __init__(
            self,
            filename,
            fps=20
    ):


        self.filename = filename


        self.fps = fps


        self.writer = None


        self.recording = False




    # --------------------------------------------------------
    # Start Recording
    # --------------------------------------------------------

    def start(
            self,
            frame
    ):


        height, width, _ = frame.shape



        # Define video codec
        fourcc = cv2.VideoWriter_fourcc(
            *"mp4v"
        )



        self.writer = cv2.VideoWriter(

            self.filename,

            fourcc,

            self.fps,

            (width, height)

        )



        self.recording = True



        print(
            "Recording Started"
        )




    # --------------------------------------------------------
    # Save Current Frame
    # --------------------------------------------------------

    def write(
            self,
            frame
    ):


        if self.recording and self.writer:


            self.writer.write(
                frame
            )




    # --------------------------------------------------------
    # Stop Recording
    # --------------------------------------------------------

    def stop(
            self
    ):


        if self.writer:


            self.writer.release()



        self.recording = False



        print(
            "Recording Saved"
        )
