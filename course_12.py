import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 像素直方图
img = cv.imread("data/apple.jpg")


color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])  # 参数为：图片、通道、mask、histSize、和ranges像素值范围
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
'''
直方图均衡化：如果一副图的像素值集中在某一个像素范围内，可以使用均衡化改变对比度
'''
gary = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
equ = cv.equalizeHist(gary)     # 需要灰度图像
cv.imshow("equal", equ)
cv.waitKey()
cv.destroyAllWindows()
