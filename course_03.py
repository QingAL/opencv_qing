import cv2 as cv
import numpy as np
# 图片的数学运算

img_1 = cv.imread("data/WindowsLogo.jpg")
img_2 = cv.imread("data/LinuxLogo.jpg")
time1 = cv.getTickCount()                       # 计算时间
img_add = cv.add(img_1, img_2)                  # 两张图片相加
img_subtract = cv.subtract(img_2, img_1)        # 两张图片相减
cv.imshow("add_demo", img_add)
cv.imshow("subtract_demo", img_subtract)
time2 = cv.getTickCount()                       # 计算时间
time = (time2 - time1)/cv.getTickFrequency()    # 计算时间
print(time)
cv.waitKey()
cv.destroyAllWindows()
