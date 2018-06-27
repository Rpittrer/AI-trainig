import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# cv.imshow("original image", img)
# cv.rectangle(img, (100, 100), (200, 200), (0, 255, 0), -1)
# cv.circle(img, (300, 300), (100), (127, 50, 127), -1)

pts = np.array([[100, 100], [200, 100], [150, 190]])
ptr = np.array([[150, 70], [100, 160], [200, 160]])
cv.polylines(img, [pts], True, (0, 255, 0), -3)
cv.polylines(img, [ptr], True, (0, 255, 0), 3)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "Arpit", (333, 333), font, 1, (250, 0, 0), 1, 1, 1)

pts = pts.reshape((-1, 1, 2))

cv.imshow('rectangle', img)

cv.waitKey(0)
cv.destroyAllWindows()
