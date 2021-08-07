import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
gray_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Original', img)
cv.imshow('GrayScale', gray_scale)
cv.waitKey(0)