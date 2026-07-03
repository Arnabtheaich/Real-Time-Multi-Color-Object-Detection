import cv2
import os

from detector import detect_objects

from utils import (
    FPS,
    draw_label,
    save_frame,
    VideoRecorder
)


# ============================================================
# CREATE OUTPUT FOLDERS
# ============================================================

os.makedirs(
    "outputs/screenshots",
    exist_ok=True
)

os.makedirs(
    "outputs/videos",
    exist_ok=True
)



# ============================================================
# CAMERA SETTINGS
# ============================================================

camera_index = 0

max_cameras = 3


cap = cv2.VideoCapture(camera_index)


if not cap.isOpened():

    print("Error: Could not open camera")

    exit()



# ============================================================
# INITIALIZE VARIABLES
# ============================================================

fps_counter = FPS()


image_number = 1

video_number = 1


recorder = None

is_recording = False



# ============================================================
# MAIN LOOP
# ============================================================

while True:


    # Read frame
    ret, frame = cap.read()


    if not ret:

        print("Failed to read frame")

        break



    # --------------------------------------------------------
    # Convert BGR frame to HSV
    # --------------------------------------------------------

    hsv_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )



    # --------------------------------------------------------
    # Object Detection
    # --------------------------------------------------------

    frame, detections = detect_objects(

        frame,

        hsv_frame,

        min_area=1500

    )



    # --------------------------------------------------------
    # FPS Counter
    # --------------------------------------------------------

    fps = fps_counter.update()


    draw_label(

        frame,

        f"FPS : {fps}",

        10,

        30

    )



    # --------------------------------------------------------
    # Object Counter
    # --------------------------------------------------------

    draw_label(

        frame,

        f"Objects : {len(detections)}",

        10,

        65

    )



    # --------------------------------------------------------
    # Controls Display
    # --------------------------------------------------------

    draw_label(

        frame,

        "Q : Quit",

        10,

        100

    )


    draw_label(

        frame,

        "S : Screenshot",

        10,

        135

    )


    draw_label(

        frame,

        "R : Record",

        10,

        170

    )


    draw_label(

        frame,

        "C : Camera",

        10,

        205

    )



    # --------------------------------------------------------
    # Recording Indicator + Save Frames
    # --------------------------------------------------------

    if is_recording:


        # Red recording dot
        cv2.circle(

            frame,

            (
                frame.shape[1] - 120,
                30
            ),

            10,

            (0, 0, 255),

            -1

        )


        draw_label(

            frame,

            "REC",

            frame.shape[1] - 100,

            40,

            (0, 0, 255)

        )



        # Save video frame
        recorder.write(frame)




    # --------------------------------------------------------
    # Display Frame
    # --------------------------------------------------------

    cv2.imshow(

        "Real-Time Multi Color Detection",

        frame

    )



    key = cv2.waitKey(1) & 0xFF



    # ========================================================
    # KEYBOARD CONTROLS
    # ========================================================


    # --------------------------
    # Quit
    # --------------------------

    if key == ord("q"):


        break




    # --------------------------
    # Screenshot
    # --------------------------

    elif key == ord("s"):


        filename = (

            f"outputs/screenshots/"
            f"screenshot_{image_number}.jpg"

        )


        save_frame(

            frame,

            filename

        )


        print(

            f"Screenshot saved: {filename}"

        )


        image_number += 1





    # --------------------------
    # Start / Stop Recording
    # --------------------------

    elif key == ord("r"):



        # Start Recording
        if not is_recording:



            filename = (

                f"outputs/videos/"
                f"recording_{video_number}.mp4"

            )



            recorder = VideoRecorder(

                filename,

                fps=20

            )



            recorder.start(frame)


            is_recording = True



            print(

                "Recording Started"

            )




        # Stop Recording
        else:



            recorder.stop()


            recorder = None


            is_recording = False


            video_number += 1



            print(

                "Recording Stopped"

            )





    # --------------------------
    # Camera Switching
    # --------------------------

    elif key == ord("c"):



        # Avoid camera change while recording
        if is_recording:


            print(

                "Stop recording before switching camera"

            )


            continue



        print(

            "Switching Camera..."

        )



        # Release current camera
        cap.release()



        # Next camera index
        camera_index += 1



        if camera_index >= max_cameras:


            camera_index = 0




        # Open new camera
        cap = cv2.VideoCapture(

            camera_index

        )



        # Camera not available
        if not cap.isOpened():



            print(

                f"Camera {camera_index} not found"

            )



            camera_index = 0



            cap = cv2.VideoCapture(

                camera_index

            )



        else:



            print(

                f"Camera switched to {camera_index}"

            )





# ============================================================
# CLEANUP
# ============================================================


# Stop recording before exit

if is_recording and recorder:


    recorder.stop()



# Release camera

cap.release()



# Close windows

cv2.destroyAllWindows()