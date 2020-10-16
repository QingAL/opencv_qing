import cv2 as cv
import numpy as np
'''
检测图片中的圆使用cv.HoughCircles
输入的值分别为灰度图像、检测圆的方法、累加器图像分辨率、两个不同圆的最小距离
param1是canny中的阈值、param2是累加器的阈值、剩下两个为最小圆和最大圆的半径
'''
img = cv.imread("data/smarties.png")
img_blur = cv.medianBlur(img, 3)
img_gray = cv.cvtColor(img_blur, cv.COLOR_BGR2GRAY)
circles = cv.HoughCircles(img_gray, cv.HOUGH_GRADIENT, 1, 25, param1=65, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))         # 返回参数取整
w = circles.shape       # 返回值是一个三维的矩阵，第一个值不知道是什么，所以下面循环第一个值为0
print(w)
for circly in circles[0, :]:
    i = circly
    cv.circle(img_gray, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv.circle(img_gray, (i[0], i[1]), 2, (0, 0, 255), 3)
cv.imshow("circlies_demo", img_gray)
cv.waitKey()
cv.destroyAllWindows()
