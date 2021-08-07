
import cv2 as cv
import numpy as np

img = np.zeros( (300,300,3), dtype='uint8')
# cv.line( img, (0,0), (300,300), (0,255,0))
# cv.line(img,(0,0), (0,300), (0,0,255), 3)
# cv.rectangle(img,(0,0),(250,250),(0,255,0),-1) / #for filled up image
cv.rectangle(img, (0,0), (img.shape[1]//2,img.shape[0]//2),(0,0,255),-1)   #anothe method
cv.imshow("My canvas",img)
cv.waitKey(0)