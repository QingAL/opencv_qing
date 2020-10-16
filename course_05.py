import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# 图像的几何变化

img = cv.imread("data/apple.jpg")
rows, cols, ch = img.shape

# 放大缩小
img_1 = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)    # fx、fy为放大倍数，interpolation为放大方法
cv.imshow("demo", img_1)

# 旋转
M = cv.getRotationMatrix2D((cols/2, rows/2), 45, 1)     # 构建旋转的矩阵M、参数为旋转中心、角度、和缩放
img_2 = cv.warpAffine(img, M, (cols*2, rows*2))             # 旋转，最后参数为展示窗口大小
cv.imshow("resize_demo", img_2)

# 仿射变换 ：原图平行的线仍然平行，所以选择3个点构建矩阵
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])         # 在原图中选择3个点，
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M_1 = cv.getAffineTransform(pts1, pts2)                 # 构建矩阵
dst = cv.warpAffine(img, M_1, (cols*2, rows*2))             # 把矩阵传入
cv.imshow("demo_12", dst)
plt.show()


cv.waitKey()
cv.destroyAllWindows()
