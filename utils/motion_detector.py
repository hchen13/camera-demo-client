import cv2
import imutils


class MotionDetector:
    def __init__(self, sensitivity=0.5):
        self.weight = 1 - sensitivity
        self.prev = None

    def update(self, frame):
        if self.prev is None:
            self.prev = frame.copy().astype("float")
            return

        cv2.accumulateWeighted(frame, self.prev, self.weight)

    def detect(self, frame, threshold=25):
        if self.prev is None:
            self.prev = frame.copy().astype('float')
            return False

        diff = cv2.absdiff(self.prev.astype("uint8"), frame)
        bin = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]
        bin = cv2.erode(bin, None, iterations=2)
        bin = cv2.dilate(bin, None, iterations=2)
        cnts = cv2.findContours(bin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        return len(cnts) > 0
