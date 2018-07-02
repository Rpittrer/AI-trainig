import cv2 as cv
import numpy as np

img = cv.imread('Hands.jpg')
h, w = img.shape[:2]

qh = h / 4
qw = w / 4
print(qh)
print(qw)
# R = np.float32([[1, 0, qh],
#                 [0, 1, qw]])
R = cv.getRotationMatrix2D((200, 200), 90, 0.5)
print(R)
rotate_img = cv.transpose(img)
img_translate = cv.warpAffine(img, R, (w, h))
cv.imshow('original', img)
cv.imshow('translate', img_translate)
cv.imshow('translate', rotate_img)
cv.waitKey(0)
cv.destroyAllWindows()
