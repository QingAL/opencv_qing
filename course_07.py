import cv2 as cv
import numpy as np

# 图像平滑 P80
img = cv.imread("data/pic2.png")
cv.imshow("original_demo", img)

# 2D卷积：定义一个5X5的矩阵
kernal = np.ones((5, 5), np.float32)/25
res = cv.filter2D(img, -1, kernal)
cv.imshow("res_demo", res)

# 平均
blur = cv.blur(img, (5, 5))
cv.imshow("blur", blur)

# 高斯模糊 ：将卷积核变为高斯核
guass = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow("gauss_demo", guass)

# 中值模糊 :常用来消除椒盐噪声
median_blur = cv.medianBlur(img, 1)
cv.imshow("median_blur", median_blur)

'''
# 双边滤波：常用来消除边界比较明显的噪声
src：输入图像
d：过滤时周围每个像素领域的直径
sigmaColor：在color space中过滤sigma。参数越大，临近像素将会在越远的地方mix。
sigmaSpace：在coordinate space中过滤sigma。参数越大，那些颜色足够相近的的颜色的影响越大。
'''
blur1 = cv.bilateralFilter(img, 1, 10, 10)
cv.imshow("blur1", blur1)

cv.waitKey()
cv.destroyAllWindows()
