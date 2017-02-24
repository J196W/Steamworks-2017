import cv2
import numpy
from camera import Camera
from settings import CameraSettings
import time
import threading

settings = CameraSettings()
frontCamera = Camera(0)
backCamera = Camera(1)
frontFrame = None
backFrame = None
pause = False
tempPause = False
settingList = None
outputsList = None



class Record(object):
    def __init__(self):
        global outputsList, settingsList
        outputsList = settings.getOut()
        settingsList = settings.getSettings()
        self.frontOut = cv2.VideoWriter(outputsList[0], settingsList[3], settingsList[0], (settingsList[1], settingsList[2]))
        self.backOut = cv2.VideoWriter(outputsList[1], settingsList[3], settingsList[0], (settingsList[1], settingsList[2]))
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        global frontCamera, backCamera, frontFrame, backFrame, pause, tempPause
        while True:
            if pause is False:
                frontFrame = frontCamera.get_frame()
                backFrame = backCamera.get_frame()
                self.frontOut.write(frontFrame)
                self.backOut.write(backFrame)

            pause = tempPause

    def end(self):
        global tempPause, frontCamera, backCamera, pause, outputsList, settingsList
        tempPause = True
        while pause is not tempPause:
            tempPause = tempPause

        self.frontOut.release()
        self.backOut.release()
        outputsList = settings.getOut()
        self.frontOut = cv2.VideoWriter(outputsList[0], settingsList[3], settingsList[0], (settingsList[1], settingsList[2]))
        self.backOut = cv2.VideoWriter(outputsList[1], settingsList[3], settingsList[0], (settingsList[1], settingsList[2]))
        

        tempPause = False

    def get_curr_frame(self, num):
        global frontFrame, backFrame
        if num == 1:
            return frontFrame
        if num == 2:
            return backFrame
