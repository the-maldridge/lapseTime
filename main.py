import camera
import time
import settings
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    capture = camera.Capture(settings.cameraID)
    while True:
        capture.updateFrame()
        capture.saveFrame(int(time.time()))
        time.sleep(settings.frameDelay)
