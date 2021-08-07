import cv2 as cv
import numpy as np

img=cv.imread('Photos/cat.jpg')                       #Reading preloaded image

blank = np.zeros((500,500,3), dtype='uint8')            #Using the numpy to create the blank image---->'uint8' is data type for image 
                                                        #  500 height, 500 width, 3 is color channel

"""
Painting an Image in different colours
"""
cv.imshow("BlaCK", blank)
# blank[:]=0,255,0                                #For Green image
# blank[:]=0,0,255                                #For Red image
# blank[:]=255,0,0                                #For blue image
blank[200:300, 300:400]=0,0,255  
cv.imshow("GREEN IMAGE",blank)
cv.waitKey(0)