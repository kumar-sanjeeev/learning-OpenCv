"""
Thresholding is nothing but the binarisation of the image, means pixels would be either zero or black, or 255 or white.
"""


import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow("cats", img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

threshold, thres_img = cv.threshold(gray,150,255,cv.THRESH_BINARY) #Wiil return thres_img as thresholded img and 
                                                                   # and threshold as thresholded value(i.e 150)
                                                                   # More the thresholded value less white color in the thresholded image
cv.imshow("Simple Thresholded", thres_img)              

threshold, thres_img_INV = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholded inverse", thres_img_INV)


#ADAPTIVE THRESHOLDING
"""
Computer will automatically find the required thresholding value --> used in more advanced cases
"""
adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive Thresholding", adaptive_threshold)

cv.waitKey(0)   