import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow("CATS", img)

# Averaging Blurr Technique
"""
Defined the kernel window over the image, and will compute the centre pixel intensity
by average outing the negibhouring pixels and similarly this window will transverse
over the image.
Higher the kernel size more blur the image is.
"""

average_blur = cv.blur(img, (3,3))
cv.imshow("Average Blue", average_blur)


# Gaussian Blurr Technique
"""
You will get the less blurring in comparison to average blurr
"""

gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian Blur", gauss)

# Meadian Blurr Technique
"""
Same as average but in this we will find the median.
More effective to reduce the noise present in the image.
Not meant for higher kernel size
"""
median = cv.medianBlur(img,3)
cv.imshow("Median Blur", median)

# Bilaternal Blurr Technique
"""
Most effective technique. Will used in advanced blurring techniques
Rest of blurring methods will start blurring without looking whether youre reducing edges in the image or not.
This method will blurr the image but do not effect the edges
"""
bilaternal=cv.bilateralFilter(img,5,15,15)
cv.imshow("Bilaternal", bilaternal)

cv.waitKey(0)