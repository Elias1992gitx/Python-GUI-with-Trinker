Python GUI for Real-time Pose Detection using MediaPipe

This Python application implements a graphical user interface (GUI) for real-time pose detection using the MediaPipe library. It provides a simple interface for capturing video from a webcam and displaying it in a tkinter window, with pose landmarks overlaid on the video feed.

Features

- Camera Control: Start and stop the camera feed with the click of a button.
- Real-time Pose Detection: Utilizes the MediaPipe library for detecting human poses in real-time.
- GUI Interface: Provides a user-friendly interface built with tkinter, making it easy to interact with the application.

Installation

1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip:-
  pip install opencv-python-headless opencv-python pillow mediapipe

1. Run the application by executing the following command:
   python camera_app.py
2. Once the application window opens, click the "Start Camera" button to initiate the camera stream.
3. The webcam feed will start, and pose landmarks will be overlaid on the video in real-time.
4. To stop the camera feed, click the "Stop Camera" button.
5. Close the application window when done.

Notes

- This application integrates tkinter for GUI development, OpenCV for camera capture and processing, Pillow for image manipulation, and MediaPipe for pose detection.
- Make sure your webcam is properly connected and accessible by your system.

Acknowledgments

This project utilizes the following libraries:

- [OpenCV](https://opencv.org/) - For capturing and processing video frames.
- [Pillow](https://python-pillow.org/) - For image manipulation.
- [MediaPipe](https://google.github.io/mediapipe/) - For real-time pose detection.



