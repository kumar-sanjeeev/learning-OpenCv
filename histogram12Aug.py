import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


"""
Histogram allows you to visulaize the pixel intensity distribution in an image.
"""
img = cv.imread('Photos/cats 2.jpg')
cv.imshow("CATS", img)

blank = np.zeros(img.shape[:2],dtype='uint8')

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('GRAY', gray)

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1);
cv.imshow("Masked", circle)

mask = cv.bitwise_and(img,img,mask=circle)


# # GRAYSCALE HISTOGRAM
  
# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

# plt.figure()
# plt.title("GRAY SCALE HISTOGRAM")
# plt.xlabel('Bins')
# plt.ylabel('No of pixels')
# plt.plot(gray_hist)
# # plt.xlim([0,256])
# plt.show()



#COLOR HISTOGRAM

plt.figure()
plt.title("COLORED HISTOGRAM")
plt.xlabel('Bins')
plt.ylabel('No of pixels')

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i], None, [256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0) 