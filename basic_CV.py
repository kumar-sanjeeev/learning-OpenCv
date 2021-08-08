import cv2 as cv
import numpy as np

img=cv.imread('Photos/group 1.jpg')
cv.imshow('Original Image',img)

#Convert image to GrayScale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY SCALE",gray)


#How to Blur an Image   ---> Is used to remove the noise present in the image
"""
Image Blurring (Image Smoothing)
Image blurring is achieved by convolving the image with a low-pass filter kernel. 
It is useful for removing noise. It actually removes high frequency content (eg: noise, edges) from the image.
So edges are blurred a little bit in this operation (there are also blurring techniques which don't blur the edges).
OpenCV provides four main types of blurring techniques.

# --> Averaging
# --> Gaussian Blurring
# --> Median Blurring  ----> It will not blur the edges of the images
# --> Bilateral Filtering

# -------------<Now we will learn Gaussian blurring>--------------------
# """
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)   # Gussian kernel is used in which we will specify the height and width of the kernel which must be positive and odd
cv.imshow('Blur Image',blur)                          # higher the value of the gussian kernel more the blur


"""
EDGE DETECTION
--------------------<Using canny Edge detection>-------------------
"""

canny = cv.Canny(img,125,175)
cv.imshow('Canny', canny)           #will show the edges of the image

#Can reduce the edges by passing the blurry image

less_edges = cv.Canny(blur,125,175)
cv.imshow('Less Canny',less_edges)


"""
Dilating the images
"""
dilated = cv.dilate(less_edges,(7,7),iterations=5)
cv.imshow('Dilated',dilated)

"""
Eroding the image
"""
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroeded',eroded)

"""
Resize the image
--> Done without taking care of aspect ratio

  # Bydefault cv.INTER_AREA interpolation will run when new size is smaller than original image
  # Use cv.INTER_LINEAR /cv.INTER_CUBIC when you try to enlarge the image to much greater size
     #cv.INTER_CUBIC is slower amongst three but will provide the high quality image

"""

resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)



""" 
Cropping the image

"""
cropped =  img[50:200, 200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)