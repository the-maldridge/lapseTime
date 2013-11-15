import cv
import logging
import json

class Capture():
    def __init__(self, camNum=0, loglevel=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.camNum = camNum
        self.cam = cv.CaptureFromCAM(self.camNum)
        self.logger.info("Opened camera {0}".format(self.camNum))

    def updateFrame(self):
        self.img = cv.QueryFrame(self.cam)
        self.logger.debug("Updated frame on camera {0}".format(self.camNum))

    def saveFrame(self, hash):
        cv.SaveImage("./images/"+str(hash) + ".png", self.img)
        self.logger.info("Saved frame with hash: {0}".format(hash))
