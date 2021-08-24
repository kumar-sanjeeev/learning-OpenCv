"""
Face Detection VS Face Recognition
Face Detection merely detects the presence of face in the image
while Face Recognition involves identifying  who face is this


Face Detection is done using the classifier.
Inbuilt OPENCV classifier for Face detection are
1. Haarcascades
2. Local Binary Patterns
"""

import cv2 as cv

img=cv.imread('Photos/lady.jpg')
cv.imshow("LADY", img)
# We don't need a color in the image for face detection for Haarcascades classifier

grey=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY PERSON", grey)

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
face_detect = haar_cascade.detectMultiScale(grey,scaleFactor =1.1, mineNeighbours=3);  #Its mnot working don't knw the reason
print(f'Number of faces detected+={len(face_detect)}')

for (x,y,w,h) in face_detect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow("Detected Faces", img )
cv.waitKey(0)