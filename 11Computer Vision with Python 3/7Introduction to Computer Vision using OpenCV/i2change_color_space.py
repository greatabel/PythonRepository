import cv2

img = cv2.imread("images/image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("images/gray_image.jpg" , gray)
cv2.imshow("image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()