import cv2 as cv
import numpy as np

img = cv.imread('Hands.jpg')
cv.imshow('hhd', img)
h, w = img.shape[:2]


qh = h / 4
qw = w / 4
print(qh)
print(qw)
T = np.float32([[1, 0, qh],
                [0, 1, qw]])
print(T)

img_translate = cv.warpAffine(img, T, (w, h))
cv.imshow('original', img)
cv.imshow('translate', img_translate)

cv.waitKey(0)
cv.destroyAllWindows()
