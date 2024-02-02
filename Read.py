import cv2 as cv
img = cv.imread('/Users/deepesh/Desktop/PROJECT/Resources/Photos/cat_large.jpg')
cv.imshow('Cats', img)

cv.waitKey(0)
capture.release()
cv.destroyAllWindows()