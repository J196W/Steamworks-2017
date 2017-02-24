import cv2
import numpy
from settings import CameraSettings

settings = CameraSettings()
settingsList = settings.getSettings()

class Camera(object):
    def __init__(self, num):
        global settingsList
        self.video = cv2.VideoCapture(num)

        self.video.set(3, settingsList[1])
        self.video.set(4, settingsList[2])
        self.video.set(5, settingsList[0])
        self.video.set(6, settingsList[3])

    def __del__(self):
        self.video.release()

    def get_frame(self):
        sucess, image = self.video.read()
        image = cv2.flip(image, 1)

        return image
