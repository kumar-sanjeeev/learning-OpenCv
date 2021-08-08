import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('Photos/lady.jpg')
cv.imshow("original", img)

#convert to gray scale----> BGR is default colorspace in cv2
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayScale',gray)

#convert BGR to HSV (Heue Saturation Value)--> like based on how human conceive colors
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#convert BGR to LAB 
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)


"""
As I have already mentioned that openCV use BGR format that is blue, green and red
to represent the images and that format is not used outside the openCV. Mostly used 
RGB format.

If we try to open the BGR image in other python library than openCV, we will observe the
color inversion problem.

"""
"""
Displaying the image using matplotlib
"""

# plt.imshow(img)
# plt.show()

#convert BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()


#HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR);
cv.imshow('HSV_BGR',hsv_bgr)
cv.waitKey(0)

"""
Few Importants points

-> Direct grayScale to LAB conversion is not possible in cv
but it can be done in two steps
Step 1: grayscale-->BGR
Step 2: BGR--->LAB
"""