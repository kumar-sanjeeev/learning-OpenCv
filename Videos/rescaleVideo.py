
import cv2 as cv

# This method will work for videos, images and Live Videos
def rescale_video(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    heigth = int(frame.shape[0]*scale)
    
    dimensions =(width,heigth)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# will only work for live videos
def change_resolution(width, height):
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Video.mp4')


while True:
    isTrue, frame = capture.read()
    resized_frame = rescale_video(frame)

    cv.imshow('Original_Video', frame)
    cv.imshow('Scaled_Video', resized_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
