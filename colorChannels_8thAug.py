import cv2 as cv
import numpy as np

"""
Every image is made up of 3 color channels i.e. Blue, Green and Red.
In CV we can split the images into different channels.
"""

img = cv.imread('Photos/cats 2.jpg')
cv.imshow("cats", img)

blank = np.zeros(img.shape[:2], dtype='uint8')


b,g,r = cv.split(img)
blue = cv.merge([b,blank,blank])
green =cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)
# merged = cv.merge([b,g,r])
# cv.imshow("Merged", merged)
# print(img.shape)
# print(b.shape)
# print(g.shape)
cv.waitKey(0)