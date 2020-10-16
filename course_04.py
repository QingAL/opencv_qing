import cv2 as cv
import numpy as np
# 色彩空间的转换和mask掩体

img_1 = cv.imread("data/smarties.png")


img_hsv = cv.cvtColor(img_1, cv.COLOR_BGR2HSV)      # 转为HSV
img_gray = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)    # 转为gray
cv.imshow("hsv_demo", img_hsv)
cv.imshow("gray_demo", img_gray)


# 在hsv色彩空间中，颜色可以更好的表示，可以使用hsv色彩空间与原图相与操作，进行目标跟踪，识别
lower_red = np.array([0, 43, 46])          # 设定HSV色彩空间中红色的值
upper_red = np.array([10, 255, 255])
mask = cv.inRange(img_hsv, lower_red, upper_red)  # 构建掩体mask
res = cv.bitwise_and(img_1, img_1, mask=mask)
cv.imshow("mask_demo", res)


cv.waitKey()
cv.destroyAllWindows()
