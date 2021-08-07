import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
gray_scale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Original', img)
cv.imshow('GrayScale', gray_scale)

# canny = cv.Canny(img, 125, 175)            #edge detection

"""
will find the contours by using the find contours method
This method will return contours and hierarchies
Mode:
cv.RETR_TREE      ----> if want to find the hierarchial contours
cv.RETER_EXTERNAL ----> if want to find the external contours
cv.RETER_LIST     ----> if want to find all contours in the list

Approximation method

cv.CHAIN_APPROX_NONE   ---> Does nothing just return all the contours
cv.CHAIN_APPROX_SIMPLE ---> commpress all the contours just returned the contour that makes more sense.
"""
# contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

# print(f'{len(contours)} contours found!!')

# blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# canny = cv.Canny(blur, 125, 175)            #edge detection in blurred image
# contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

# print(f'{len(contours)} contours found!!')

# Now we will see how contours number has been decreased just by blurring the image

# cv.imshow('Canny', canny)        

"""
Now will use the threshold method to find the contours in the image.
it will take attempt to binarise the image
if value of particular pixel density is less thatn threshold value ---> then it becomes 0 (i.e. black)
Rest all pixels above threshold becomes white (i.e 1)
""" 

ret, thres = cv.threshold(gray_scale, 125, 255,cv.THRESH_BINARY)       # 125 is the threshold value

contours, hierarchies = cv.findContours(thres,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours found!!')
cv.imshow("Binary Image", thres)


"""
With the help of NUMPY we can visualise the contours that we found in the image
"""
blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank Image',blank)

# Drawing the contours over the blank image
cv.drawContours(blank, contours, -1,(0,0,255),1)
cv.imshow('Contours', blank)
cv.waitKey(0)