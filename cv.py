import cv2

img = cv2.imread('Hands.jpg')

#cv2.imshow("hello world", img)
print(img.shape)
cv2.waitKey(0)

cv2.destroyAllWindows()
