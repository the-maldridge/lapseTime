import camera
import time
import settings
import logging

def run():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Welcome to LapseTime".center(45, '='))
    capture = camera.Capture(settings.cameraID)
    while True:
        try:
            capture.updateFrame()
            capture.saveFrame(int(time.time()))
            time.sleep(settings.frameDelay)
        except KeyboardInterrupt:
            logger.warning("C-c was recieved")
            exit()
        except:
            logger.error("An error occured or C-c was keyed -- EXITING!")
            exit()

if __name__ == "__main__":
    run()
