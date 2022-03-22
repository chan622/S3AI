import cv2
img = cv2.imread('lena.jpg')
cv2.imshow('lena', img)
cv2.waitKey(1000)
cv2.destroyAllWindows()