import cv2 as cv
import cv2
import numpy as np

#img = cv.imread('/Users/deepesh/Desktop/PROJECT/Resources/Photos/cat_large.jpg')
img = np.zeros((512, 512, 3), dtype=np.uint8)
img=cv2.line(img,(0,0),(255,255),(0,0,255),5) 
#arrowedLine
img=cv2.rectangle(img,(384,0),(512,128),(0,0,255),5) 
img=cv2.circle(img,(447,63),63,(0,0,255),-1) 
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'opencv',(10,500),font,4,(255,255,255),10,cv2.LINE_AA) 
cv.imshow('Cats', img)

cv.waitKey(0)
capture.release()
cv.destroyAllWindows()