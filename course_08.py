import cv2 as cv
import numpy as np

# 形态学转化 P84
img = cv.imread("data/LinuxLogo.jpg")
cv.imshow("originial", img)
kernal_1 = np.ones((3, 3), np.uint8)
'''
# 腐蚀erosion
erosion = cv.erode(img, kernal_1)
cv.imshow("erosion_demo", erosion)

# 膨胀dilation
dilation = cv.dilate(img, kernal_1)
cv.imshow("dilation_demo", dilation)

# 开运算：先腐蚀，再膨胀
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernal_1)
cv.imshow("opening_demo", opening)

# 闭运算：先膨胀，再腐蚀
closing = cv.morphologyEx(img, cv.MORPH_CLOSE,kernal_1)
cv.imshow("closing_demo", closing)
'''
# 形态学梯度：即膨胀和腐蚀的差别
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernal_1)
cv.imshow("gradient_demo", gradient)

cv.waitKey()
cv.destroyAllWindows()
