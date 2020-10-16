import cv2 as cv
import numpy as np

# 高斯图像金字塔 P99
img = cv.imread("data/messi5.jpg")
lower_img01 = cv.pyrDown(img)           # 缩小
lower_img02 = cv.pyrDown(lower_img01)
cv.imshow("lower_img", lower_img01)
cv.imshow("lower_img02", lower_img02)

upper_img01 = cv.pyrUp(img)             # 放大
upper_img02 = cv.pyrUp(upper_img01)
cv.imshow("upper_img01", upper_img01)
cv.imshow("upper_img02", upper_img02)


cv.waitKey()
cv.destroyAllWindows()
