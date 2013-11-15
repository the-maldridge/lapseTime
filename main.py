import camera
import cv
import time
import settings
import logging

def run():
    interval=0
    logging.basicConfig(level=settings.loglevel)
    logger = logging.getLogger(__name__)
    logger.info("Welcome to LapseTime".center(45, '='))
    capture = camera.Capture(settings.cameraID)
    while True:
        try:
            capture.updateFrame()
            if (interval%settings.frameDelay==0):
                capture.saveFrame(int(time.time()))
                interval=0
            interval=interval+1
            time.sleep(1)
        except KeyboardInterrupt:
            logger.warning("C-c was recieved")
            exit()

if __name__ == "__main__":
    run()
