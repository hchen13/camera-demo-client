from datetime import datetime
from time import sleep

import cv2
from imutils import resize
from imutils.video import VideoStream

from utils import Connector, MotionDetector, draw_vips, display_fps

if __name__ == '__main__':
    feed = True
    host = '47.108.136.249'

    con = Connector(host)
    motion = MotionDetector(sensitivity=.5)

    vs = VideoStream().start()
    sleep(2.)

    t_0 = datetime.now()
    frame_count = 0
    while True:
        frame = vs.read()
        frame = resize(frame, width=778)
        print("[info] frame size: {}".format(frame.shape))

        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if motion.detect(grayscale):
            tick = datetime.now()
            results = con.query(frame)
            tock = datetime.now()
            print("[info] querying results takes {}".format(tock - tick))
            if feed:
                draw_vips(frame, results, padding=10)

        motion.update(grayscale)

        frame_count += 1
        elapsed = (datetime.now() - t_0).total_seconds()
        fps = frame_count / elapsed
        print("FPS:", fps)
        if feed:
            display_fps(frame, fps)
        if frame_count > 1000:
            frame_count = 0
            t_0 = datetime.now()

        if feed:
            cv2.imshow('live', frame)
        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):
            break

        print()
