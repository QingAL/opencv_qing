import cv2 as cv
import numpy as np

# 多对象的模版匹配
img = cv.imread("data/smarties.png")
img_template = cv.imread("data/smarty_red.png")
h, w = img_template.shape[:2]
thresould = 0.9     # 匹配相似度大于0.9的模版
res = cv.matchTemplate(img, img_template, cv.TM_CCOEFF_NORMED)
loc = np.where(res >= thresould)
for index in zip(*loc[::-1]):
    bottom_right = (index[0]+h, index[1]+w)
    cv.rectangle(img, index, bottom_right, (0, 0, 0), 2)
cv.imshow("img_matched", img)


cv.waitKey()
cv.destroyAllWindows()
