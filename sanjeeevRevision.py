import cv2 as cv
import numpy as np

"""
Tutorial No 1 ----------Basics
"""
# How to read image present in the same directory
img = cv.imread('Photos/cats.jpg')
cv.imshow("cats original", img)

# How to convert into gray scale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale without blur', gray_img)

#How to blur the image
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Gaussian Blur', blur)

blur_gray = cv.GaussianBlur(gray_img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blurred with gray', blur_gray)

# How to detect the edges in the image
canny = cv.Canny(blur_gray,125,175)
cv.imshow("Canny without blur", canny)

#Resizing of Image  -----> but will be done without taking care of aspect ratio of image
resized_img = cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized Image',resized_img)

"""
Tutorial No 2----------Draw 
"""

#How to draw the blank image
blank = np.zeros((500,500,3), dtype='uint8')

blank [:] = 255,0,0
blank[200:300, 300:400]=0,0,255
cv.imshow("Blank", blank)

"""
Tutorial No 3 -----------Draw Shapes
"""
rect = cv.rectangle(blank, (0,0), (img.shape[1]//2, img.shape[0]//2),(0,255,0),-1)
cv.imshow('Rectangle', rect)

circle = cv.circle(img,(200,150),40,(0,0,255),3)
cv.imshow('Circle',circle)

"""
Tutorial No 4 --> Transformations
"""

# creating the linear transformation function

def trans(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1]),(img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated_img = trans(img, 100, 150)
cv.imshow("Translated img",translated_img)


# creating the rotation function

def rot(img, angle, rotPoint = None):
    dimensions = (img.shape[1], img.shape[0])
    if (rotPoint==None):
        rotPoint = (img.shape[1]//2, img.shape[0]//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1)
    return cv.warpAffine(img,rotMat,dimensions)

rotated_img = rot(img, 180)
cv.imshow("Rotated Image",rotated_img)

cv.waitKey(0)