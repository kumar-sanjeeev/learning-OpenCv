from typing import ItemsView
import cv2 as cv
import numpy as np

img = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('My_image',img)

# #Drawing a rectangle
# cv.rectangle(img, (0,0), (img.shape[1]//2,img.shape[0]//2),(0,255,0),-1)
# cv.imshow('Rectangle', img)

# #Drawing a circle
# cv.circle(img, (250,250), 40, (0,0,255), -1)

# cv.imshow("Figures",img)
# #Draew the white line having thickness 3
# cv.line(img, (0,0), (250,250), (255,255,255), 3)
# cv.imshow('More figures', img)

#Put the text on the image
cv.putText(img, "My name is Sanjeev",(100,100), cv.FONT_HERSHEY_TRIPLEX, 0.75, (255,0,0), 2)
cv.imshow('Info',img)
cv.waitKey(0)