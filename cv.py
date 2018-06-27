import c2 as cv
img = cv.imread('Hands.jpg')

#cv.imshow("hello world", img)
B,G,R = cv.split(img)

zeroes = np.zeros(img.shape[:2], dtype="uint8")

cv.imshow("red",cv.merge([zeroes,zeroes,R]))
cv.imshow("green",cv.merge([zeroes,G,zeroes]))
cv.imshow("blue",cv.merge([B,zeroes,zeroes]))
cv.imshow("purple",cv.merge([B,zeroes,R]))
cv.imshow("gyg",cv.merge([zeroes,G,R]))
cv.imshow("hy",cv.merge([B,G,R]))

# print(img.shape)
# ret, thresh1 = cv.threshold(img,50,255,cv.THRESH_BINARY)
# #ret, thresh2 = cv.threshold(img,50,255,cv.THRESH_BINARY_INV)
# cv.imshow("n545n",thresh1)
# #cv.imshow("nn",thresh2)

# img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow('hsv image',img_hsv)
# cv.imshow('hue',img_hsv[:,:,0])
# cv.imshow('sat',img_hsv[:,:,1])
# cv.imshow('value',img_hsv[:,:,2])

cv.waitKey(0)
cv.destroyAllWindows()
