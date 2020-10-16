import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("data/coins.jpg")
# cv.imshow("coins", img)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)      # 变为gray

ret, thresh = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)   # 二值化
cv.imshow("thresh", thresh)

kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)  # 进行开运算
img_bg = cv.dilate(opening, kernel, iterations=3)  # 膨胀
cv.imshow("img_bg", img_bg)

dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)   # 距离运算
ret, img_fg = cv.threshold(dist_transform, 0.1 * dist_transform.max(), 255, 0)
cv.imshow("img_fg", img_fg)

img_fg = np.uint8(img_fg)
unknow = cv.subtract(img_bg, img_fg)
cv.imshow("unknow", unknow)
ret, markers = cv.connectedComponents(img_fg, connectivity=8)
markers = markers + 1

markers[unknow == 255] = 0

markers = cv.watershed(img, markers)  # 分水岭算法后，所有轮廓的像素点被标注为 -1
print(markers)

img[markers == -1] = [0, 0, 255]   # 标注为-1 的像素点标 红
cv.imshow("dst", img)

cv.waitKey()
cv.destroyAllWindows()
