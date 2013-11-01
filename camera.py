import cv
import logging
import json

class Capture():
    def __init__(self, camNum=0):
        self.camNum = camNum
        self.cam = cv.CaptureFromCAM(self.camNum)
        logging.info("Opened camera {0}".format(self.camNum))

    def updateFrame(self):
        self.img = cv.QueryFrame(self.cam)
        logging.info("Updated frame on camera {0}".format(self.camNum))

    def saveFrame(self, hash):
        cv.SaveImage(str(hash) + ".png", self.img)
        logging.info("Saved frame with hash: {0}".format(hash))
