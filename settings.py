import time
import cv2

FPS = 30
WIDTH = 1280
HEIGHT = 720
CODEC = cv2.VideoWriter_fourcc(*'MPEG')

frontName = None
backName = None
frontOut = None
backOut = None

class CameraSettings(object):
    def getOut(self):
        global frontName, backName, FPS, WIDTH, HEIGHT, CODEC, frontOut, backOut
        frontName = time.strftime("%I-%M-%d") + "-FRONT.mp4"
        backName = time.strftime("%I-%M-%d") + "-BACK.mp4"
    
        names = [frontName, backName]

        return names

    def getSettings(self):
        global FPS, WIDTH, HEIGHT, CODEC
        settings = [FPS, WIDTH, HEIGHT, CODEC]
        
        return settings
