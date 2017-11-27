import cv2

img = cv2.imread("images/image.jpg")
cv2.imwrite("images/saved.jpg" , img)