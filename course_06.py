import cv2 as cv

# 图像阈值 P67
img = cv.imread("data/board.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY_demo", img_gray)


# 简单阈值：当像素值高于某个阈值时，赋予他一种新的颜色
ret, thresh1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
cv.imshow("thresh_demo", thresh1)   # 当灰度值高于127时，转化为255


cv.waitKey()
cv.destroyAllWindows()
