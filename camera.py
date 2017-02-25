import cv2
import numpy

class Camera(object):
    def __init__(self, num):
        self.video = cv2.VideoCapture(num)

        self.video.set(3, 640)
        self.video.set(4, 360)
        self.video.set(5, 30)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        sucess, image = self.video.read()
        image = cv2.flip(image, 1)

        return image
