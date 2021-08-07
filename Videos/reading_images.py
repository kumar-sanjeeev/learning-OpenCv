import cv2 as cv      #importing the openCv library

#img = cv.imread('Photos/cat.jpg')     #imread is used to take the image input and then return the matrix val of the pixels

img = cv.imread('Photos/cat_large.jpg') # now I am reading the larger picture
                                        # As this image is very large --> not able to captured in the current computer screen

cv.imshow('CAT', img)                 #imshow is used to show the captured pixels (in variable) in new window named "CAT"

cv.waitKey(0)                         #brief wait for the keyboard key to be pressed