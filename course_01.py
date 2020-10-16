import cv2 as cv
import numpy as np
# 图片的基本操作

img = cv.imread("data/ml.png")      # 读取图片
cv.imshow("img_demo", img)          # 显示图片
pixel = img[100, 100]               # 一个点的像素值，输出顺序为BGR
pixel_blue = img[100, 100, 0]       # 一个像素点的Blue值
print(pixel)
print(pixel_blue)
print(img.shape)                    # 获取图像的行数、列数，以及通道
print(img.size)                     # 返回像素值的个数
print(img.dtype)                    # 返回图像的数据类型
cv.waitKey()
cv.destroyAllWindows()
