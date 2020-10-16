import cv2 as cv
import numpy as np

# canny边缘检测 P91
img = cv.imread("data/messi5.jpg")
cv.imshow("original", img)


canny = cv.Canny(img, 100, 200)
cv.imshow("canny_demo", canny)


cv.waitKey()
cv.destroyAllWindows()
