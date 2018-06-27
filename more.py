import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv.imshow("original image", img)
# cv.rectangle(img, (100, 100), (200, 200), (0, 255, 0), -1)
# cv.circle(img, (300, 300), (100), (127, 50, 127), -1)

pts = np.array([[100, 100], [300, 90], [400, 500]], )
cv.polylines(img, [pts], True, (0, 255, 0), 1)

pts = pts.reshape((-1, 1, 2))

cv.imshow('rectangle', img)

cv.waitKey(0)
cv.destroyAllWindows()
