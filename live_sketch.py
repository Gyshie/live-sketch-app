import cv2 #import OpenCV
import numpy as np #import Numpy

def sketch(image):
    #Converting image to grayscale
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #Blur the image using Gaussian Blur
    img_blur=cv2.GaussianBlur(img_gray,(3,3),0)
    #Detect edges
    edges=cv2.Canny(img_blur,10,80)
    #Invert threshold
    ret,mask=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
    return mask

#Reading frame from the webcam
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('Live_Sketch',sketch(frame))
    # Key13==ENTER_KEY
    if cv2.waitKey(1)==13:
        break
#Releasing_webcam
cap.release()
#Destroying_window
cv2.destroyAllWindows()