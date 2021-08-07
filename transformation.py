import cv2 as cv
import numpy as np

img = cv.imread('Photos/group 1.jpg')

cv.imshow('original',img)


# # <--------For Translation------------------>


# def translate(img, x, y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)

# """
# <--------Transformation--------->
# -x == Left
# +x == Right
# -y == Up
# +y == Down

# """

# translated_img = translate(img, 100, 100)
# cv.imshow('Translated Image', translated_img)


# <--------For Rotation------------------>

# def rotate(img, angle, rotPoint = None):
#     dimensions = (img.shape[1], img.shape[0])
#     if (rotPoint == None):
#         rotPoint = ((img.shape[1])//2,(img.shape[0])//2)
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     return cv.warpAffine(img, rotMat, dimensions)

# """ 
# +---> will rotate ACW
# - --> will roate CW
# """
# rotated_img = rotate(img, -180)
# rr_img = rotate(rotated_img,-45)

# rr_img2 =rotate(img, -90)
# cv.imshow('-45 image',rotated_img)
# cv.imshow('-45 & -45',rr_img)
# cv.imshow('-90 image',rr_img2)

# <--------Resizing of Image------------------>

# resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
# cv.imshow('Resized',resized)

# <-------Flipping of Image------------------>

# """
# Flipcode
# 0 --> flip vertically --> means over x axis
# 1 --> flip horizontally --> means over y axis
# -1 --> flips vertically and horizontally both (i.e over x and y axis)   (same as -180 rotation about centre of image)
# """

# fliped_img = cv.flip(img,-1)
# cv.imshow('Flipped Image',fliped_img)

# <-------Cropping of Image------------------>

cropped = img[200:300, 300:400]
cv.imshow("Cropped",cropped)

cv.waitKey(0)