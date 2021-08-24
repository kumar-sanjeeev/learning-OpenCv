import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow("CATS", img)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#LAPLACIAN--->Gradient measurement method No 1
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("LAPLACIAN", lap)


#Soble-->Gradient measurement method No 2, Calculate the gradient in x and y direction
sobelX= cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY= cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelX, sobelY)

cv.imshow("COMBINED SOBEL", combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("CANY", canny)
cv.waitKey(0)