import cv2 as cv

'''
模版匹配使用cv.TM_CCOEFF方法此外还有
cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED
cv2.TM_SQDIFF和cv2.TM_SQDIFF_NORMED匹配点是最小值，应该使用min_index
'''

img = cv.imread("data/messi5.jpg")
img_face = cv.imread("data/messi_face.jpg")
w, h, c = img_face.shape
res = cv.matchTemplate(img, img_face, cv.TM_CCOEFF)     # 参数为图片，模版和方法
min_val, max_val, min_index, max_index = cv.minMaxLoc(res)
top_left = max_index
bottom_right = (top_left[0]+h, top_left[1]+w)
cv.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)   # 在图像上画矩阵，基于match的max_index
cv.imshow("matched", img)
cv.imshow("face_demo", img_face)


cv.waitKey()
cv.destroyAllWindows()
