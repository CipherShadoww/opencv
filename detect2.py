import cv2 as cv
import cv2
import numpy as np 
def nothing(x):
    pass


def calculate_distance(known_size, focal_length, measured_size):
    distance = (known_size * focal_length) / measured_size
    return distance


def get_color_name(average_color):

    red_range = np.array([[0, 100, 100], [10, 255, 255]])
    green_range = np.array([[40, 100, 100], [80, 255, 255]])
    blue_range = np.array([[110, 100, 100], [130, 255, 255]])

    if average_color[0] <= 10 and 100 <= average_color[1] <= 255 and 100 <= average_color[2] <= 255:
        return "Red"
    elif 40 <= average_color[0] <= 80 and 100 <= average_color[1] <= 255 and 100 <= average_color[2] <= 255:
        return "Green"
    elif 110 <= average_color[0] <= 130 and 100 <= average_color[1] <= 255 and 100 <= average_color[2] <= 255:
        return "Blue"
    else:
        return "Unknown" 
    

#cap = cv2.VideoCapture(0);
cv2.namedWindow("tracking")
cv2.createTrackbar("lv","tracking",0,255,nothing)
cv2.createTrackbar("uv","tracking",0,255,nothing)
knownsize = 0.1 # just for example
focallength = 500.0      

while(True):
   # ret,frame=cap.read()
    frame=cv.imread("/Users/deepesh/Downloads/images.jpeg")
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lv=cv2.getTrackbarPos("lv","tracking")
    uv=cv2.getTrackbarPos("uv","tracking")
    ret,thresh=cv2.threshold(gray,lv,uv,cv2.THRESH_BINARY)
    contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour in contours:
       approx=cv2.approxPolyDP(contour,0.001*cv2.arcLength(contour,True),True)
       cv2.drawContours(frame,[approx],0,(0,255,0),5)
       
       x, y, w, h = cv.boundingRect(approx)
  
       average_color = np.mean(hsv_frame[y:y+5, x:x+5], axis=(0, 1))
       measuredsize = max(w, h)
    
       distance = calculate_distance(knownsize, focallength, measuredsize)

       if len(approx)==3:
          cv2.putText(frame,f"Triangle-{get_color_name(average_color)}",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
          cv2.putText(frame,f"width"+str(w),(x,y+20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
          cv2.putText(frame,f"height"+str(h),(x,y+40),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
       elif len(approx)==4:
          x,y,w,h=cv2.boundingRect(approx)
          asspect=float(w/h)
          if asspect >=0.9 and asspect<=1.1:
            cv2.putText(frame,f"Square-{get_color_name(average_color)}",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
            cv2.putText(frame,f"width"+str(w),(x,y+20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
            cv2.putText(frame,f"height"+str(h),(x,y+40),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
          else:
            cv2.putText(frame,f"Rectangle-{get_color_name(average_color)}",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
            cv2.putText(frame,f"width"+str(w),(x,y+20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
            cv2.putText(frame,f"height"+str(h),(x,y+40),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

       elif len(approx)==5:
            cv2.putText(frame,f"Pentagon-{get_color_name(average_color)}",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
            cv2.putText(frame,f"width"+str(w),(x,y+20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
            cv2.putText(frame,f"height"+str(h),(x,y+40),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
       else:
          cv2.putText(frame,f"circle-{get_color_name(average_color)}",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
          cv2.putText(frame,f"width"+str(w),(x,y+20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
          cv2.putText(frame,f"height"+str(h),(x,y+40),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))


 


    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
      break





capture.release()
cv.destroyAllWindows()