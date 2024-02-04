import cv2 as cv
import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0);
cv2.namedWindow("tracking")
cv2.createTrackbar("lv","tracking",150,255,nothing)
cv2.createTrackbar("uv","tracking",255,255,nothing)
while(True):
    ret,frame=cap.read()
    #frame=cv.imread("/Users/deepesh/Downloads/50+ Shapes Name in English with Pictures » Onlymyenglish_com.jpg")
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    lv=cv2.getTrackbarPos("lv","tracking")
    uv=cv2.getTrackbarPos("uv","tracking")

    canny=cv2.Canny(gray,lv,uv)
    kernel=np.ones((3,3))
    dilated=cv2.dilate(canny,kernel,iterations=1)#removing noise

   # ret,thresh=cv2.threshold(gray,lv,uv,cv2.THRESH_BINARY)
    contours,hierarchy=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
       
       area=cv2.contourArea(contour)
       if area>1000:
        cv2.drawContours(frame,contour,-1,(0,255,0),5)
       peri=cv2.arcLength(contour,True)
       approx=cv2.approxPolyDP(contour,0.01*peri,True)
       x,y,w,h=cv2.boundingRect(approx)
       
       # cv2.rectangle()
       if len(approx)==3:
          #cv2.putText(frame,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))
          cv2.putText(frame,str(len(approx)),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))
       elif len(approx)==4:
          x,y,w,h=cv2.boundingRect(approx)
          asspect=float(w/h)
          if asspect >=0.9 and asspect<=1.1:
           # cv2.putText(frame,"Square",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))
            cv2.putText(frame,str(len(approx)),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))
          else:
            #cv2.putText(frame,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))
            cv2.putText(frame,str(len(approx)),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))

       elif len(approx)==5:
            #cv2.putText(frame,"Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))
            cv2.putText(frame,str(len(approx)),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))
       else:
          #cv2.putText(frame,"circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))
          cv2.putText(frame,str(len(approx)),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0))


 

    cv2.imshow('canny',canny)
    cv2.imshow('dilate',dilated)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
      break





capture.release()
cv.destroyAllWindows()