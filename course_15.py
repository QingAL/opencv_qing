import cv2 as cv
import numpy as np
'''
P163
直线检测：ρ = x cos θ + y sin θ
gray-canny变化
cv.HounghLines()方法中返回值是ρ长度和θ角度
'''
img = cv.imread("data/sudoku.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_edge = cv.Canny(img_gray, 50, 150, apertureSize=3)
cv.imshow("edge", img_edge)
lines = cv.HoughLines(img_edge, 1, np.pi/180, 200)  # ρ和theta的精度，200为阈值，高于阈值才被认为是一条直线
for line in lines:
    rho, theta = line[0]    # 获取极值ρ长度和θ角度
    a = np.cos(theta)   # 获取角度cos值
    b = np.sin(theta)   # 获取角度sin值
    x0 = a*rho          # 获取x轴值
    y0 = b*rho          # 获取y轴值   x0和y0是直线的中点
    x1 = int(x0 + 1000*(-b))    # 计算直线最大值
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))    # 计算直线最小值
    y2 = int(y0 - 1000*(a))
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)    # 标注直线
cv.imshow("line", img)


cv.waitKey()
cv.destroyAllWindows()
