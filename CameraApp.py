import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np
import mediapipe as mp


class CameraApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Camera App")

        self.camera = cv2.VideoCapture(0)

        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        self.btn_start_camera = tk.Button(window, text="Start Camera", command=self.start_camera)
        self.btn_start_camera.pack()

        self.btn_stop_camera = tk.Button(window, text="Stop Camera", command=self.stop_camera, state="disabled")
        self.btn_stop_camera.pack()

        self.is_camera_running = False
        self.mp_holistic = mp.solutions.holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)  # Bind closing event

    def start_camera(self):
        if not self.is_camera_running:
            self.is_camera_running = True
            self.btn_start_camera.config(state="disabled")
            self.btn_stop_camera.config(state="normal")
            self.capture()

    def stop_camera(self):
        if self.is_camera_running:
            self.is_camera_running = False
            self.btn_start_camera.config(state="normal")
            self.btn_stop_camera.config(state="disabled")

    def capture(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Perform Mediapipe detection
            frame, results = self.mediapipe_detection(frame)

            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
            self.canvas.image = img

            if self.is_camera_running:
                self.window.after(10, self.capture)

    def mediapipe_detection(self, image):
        image.flags.writeable = False
        results = self.mp_holistic.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        self.draw_styled_landmarks(image, results)
        return image, results

    def draw_styled_landmarks(self, image, results):
        mp.solutions.drawing_utils.draw_landmarks(
            image, results.face_landmarks, mp.solutions.holistic.FACEMESH_TESSELATION,
            mp.solutions.drawing_utils.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
            mp.solutions.drawing_utils.DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1)
        )

        mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, mp.solutions.holistic.POSE_CONNECTIONS)
        mp.solutions.drawing_utils.draw_landmarks(image, results.left_hand_landmarks,
                                                  mp.solutions.holistic.HAND_CONNECTIONS)
        mp.solutions.drawing_utils.draw_landmarks(image, results.right_hand_landmarks,
                                                  mp.solutions.holistic.HAND_CONNECTIONS)

    def on_closing(self):
        self.window.destroy()
        self.camera.release()


if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()







# import tkinter as tk
# import cv2
# from PIL import Image, ImageTk
#
# class CameraApp:
#     def __init__(self, window):
#         self.window = window
#         self.window.title("Camera App")
#
#         self.camera = cv2.VideoCapture(0)
#
#         self.canvas = tk.Canvas(window, width=640, height=480)
#         self.canvas.pack()
#
#         self.btn_start_camera = tk.Button(window, text="Start Camera", command=self.start_camera)
#         self.btn_start_camera.pack()
#
#         self.btn_stop_camera = tk.Button(window, text="Stop Camera", command=self.stop_camera, state="disabled")
#         self.btn_stop_camera.pack()
#
#         self.is_camera_running = False
#
#         self.window.protocol("WM_DELETE_WINDOW", self.on_closing)  # Bind closing event
#
#     def start_camera(self):
#         if not self.is_camera_running:
#             self.is_camera_running = True
#             self.btn_start_camera.config(state="disabled")
#             self.btn_stop_camera.config(state="normal")
#             self.capture()
#
#             print("camera initiated")
#
#     def stop_camera(self):
#         if self.is_camera_running:
#             self.is_camera_running = False
#             self.btn_start_camera.config(state="normal")
#             self.btn_stop_camera.config(state="disabled")
#
#     def capture(self):
#         ret, frame = self.camera.read()
#         if ret:
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             img = Image.fromarray(frame)
#             img = ImageTk.PhotoImage(image=img)
#             self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
#             self.canvas.image = img
#             if self.is_camera_running:
#                 self.window.after(10, self.capture)
#
#     def on_closing(self):
#         self.window.destroy()
#         self.camera.release()
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CameraApp(root)
#     root.mainloop()