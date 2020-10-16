import cv2 as cv
import numpy as np

# 图像梯度 边缘检测
img = cv.imread("data/cards.png")

# laplacian算子
laplacian = cv.Laplacian(img, -1)       # ddepth图像深度，即输出图像的数据类型
cv.imshow("laplacian_demo", laplacian)

# sobel算子
sobelX = cv.Sobel(img, -1, 1, 0, ksize=5)   # 在x方向求导
cv.imshow("sobelX_demo", sobelX)
sobelY = cv.Sobel(img, -1, 0, 1,ksize=5)    # 在y方向求导
cv.imshow("sobelY_demo", sobelY)


cv.waitKey()
cv.destroyAllWindows()
