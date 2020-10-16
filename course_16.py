import cv2 as cv
import numpy as np
'''
另一种直线检测方法
cv.HounghLines()方法中，每一条直线都要用到两个参数，这需要大量的计算
cv.HounghLinesP()方法中返回值为为线的参数
'''
img = cv.imread("data/sudoku.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_canny = cv.Canny(img_gray, 50, 100, apertureSize=3)
minlinelength = 100
maxlinegap = 30
lines = cv.HoughLinesP(img_canny, 1, np.pi/180, 100, minlinelength, maxlinegap)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imshow("line_demo", img)


cv.waitKey()
cv.destroyAllWindows()