import cv2 as cv
import numpy as np

img = cv.imread('Hands.jpg')
cv.imshow("original", img)

kernel_3x3 = np.ones((3, 3), np.float32) / 9
blur = cv.filter2D(img, -1, kernel_3x3)

cv.imshow("blur", blur)

cv.waitKey(0)
cv.destroyAllWindows()
