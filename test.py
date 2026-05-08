import numpy as np
import cv2 as cv

cap = cv.VideoCapture("C:/Users/TibO/Videos/Timeline 3.mov")
# cap = cv.VideoCapture("C:/Users/TibO/Videos/Wall-E.2008.1080P.Brrip.X264.Yify.mp4")
# cap.set(cv.COLOR_BGR2RGBA, "BGR2RGBA")

while cap.isOpened():
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
