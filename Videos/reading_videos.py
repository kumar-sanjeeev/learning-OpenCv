import cv2 as cv

capture = cv.VideoCapture('Videos/dog.mp4')        #it will take intger as argument(if your webcam/other cam is connected) or path of the video as argument 

#loop is required to run the video, as it will be played frame by frame

while True:
    (isTrue, frame)= capture.read()      # to read the frame of the video
    cv.imshow('Dog_Video', frame)        # same as img, used to read the captured frame

    if cv.waitKey(20) & 0xFF==ord('d'):  # to break the while loop   
        break
capture.release()                        #used to release the capture variable
cv.destroyAllWindows()                   #used to destroy all open windows



"""
(-215:Assertion failed)---> This error is thrown in the last bcz opencv is unable to locate the frame

----->This error will also occur if you provide the wrong path of the image and video

"""


                                  