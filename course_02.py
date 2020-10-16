import cv2 as cv
import numpy as np
# ROI区域、图像的分离与合并

img = cv.imread("data/board.jpg")
cv.imshow("demo", img)


ROI = img[0:65, 0:44]                       # 选择图像中的一块区域
cv.imshow("ROI_demo", ROI)                  # ROI区域region of interest 感兴趣区域


b, g, r = cv.split(img)                     # 图像的分离与合并
cv.imshow("b_demo", b)                      # 使用split()分离出BGR
cv.imshow("g_demo", g)
cv.imshow("r_demo", r)
bgr = cv.merge([b, g, r])                   # 使用mergen()合并
cv.imshow("BGR", bgr)


img[:, :, 2] = 0                            # 使img的3通道R值为零
cv.imshow("BG_demo", img)


bigger = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_REFLECT)    # 图像扩边 img为输入图像，
cv.imshow("bigger_demo", bigger)             # 下面4个参数为边界对应的像素数，最后一个为边界的类型cv.BORDER_REFLECT为边界的镜像


cv.waitKey()
cv.destroyAllWindows()
