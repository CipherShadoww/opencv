import cv2 as cv
import cv2
def nothing(x):
    pass

cap = cv2.VideoCapture(0);
cv2.namedWindow("tracking")
cv2.createTrackbar("lv","tracking",0,255,nothing)
cv2.createTrackbar("uv","tracking",0,255,nothing)
while(True):
    ret,frame=cap.read()
    #frame=cv.imread("/Users/deepesh/Downloads/images.jpeg")
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    lv=cv2.getTrackbarPos("lv","tracking")
    uv=cv2.getTrackbarPos("uv","tracking")
    ret,thresh=cv2.threshold(gray,lv,uv,cv2.THRESH_BINARY)
    contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour in contours:
       approx=cv2.approxPolyDP(contour,0.001*cv2.arcLength(contour,True),True)
       cv2.drawContours(frame,[approx],0,(0,0,0),5)
       x=approx.ravel()[0]
       y=approx.ravel()[1]
       if len(approx)==3:
          cv2.putText(frame,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
       elif len(approx)==4:
          x,y,w,h=cv2.boundingRect(approx)
          asspect=float(w/h)
          if asspect >=0.9 and asspect<=1.1:
            cv2.putText(frame,"Square",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
          else:
            cv2.putText(frame,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))

       elif len(approx)==5:
            cv2.putText(frame,"Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
       else:
          cv2.putText(frame,"circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))


 


    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
      break





capture.release()
cv.destroyAllWindows()