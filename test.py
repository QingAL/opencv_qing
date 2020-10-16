import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    cv.imshow("demo", frame)
    c = cv.waitKey(30)
    if c == 27:
        break
cv.destroyAllWindows()
