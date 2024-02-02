

import cv2 as cv
import cv2

cap = cv2.VideoCapture(0);
while(True):
    ret,frame=cap.read()
    #frame=cv.imread("/Users/deepesh/Downloads/cv/samples/data/opencv-logo.png")    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,127,255,0)
    contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#CONTOURS IS A NUMPY ARRAY
    print("number of contours="+str(len(contours)))
    #print(contours[0])
    cv2.drawContours(frame,contours,-1,(0,255,0),3) #-1=all draw
    cv2.imshow('gray',gray)
    cv2.imshow('image',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
      break
capture.release()
cv.destroyAllWindows()