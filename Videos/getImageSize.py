import cv2 as cv

img = cv.imread('Photos/cat.jpg')

dimension = img.shape
height= img.shape[0]
width= img.shape[1]

print("Image Dimensions: ",dimension)
print("Height of Image is: ",height)
print("Width of image is: ",width)