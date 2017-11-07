import cv2

img = cv2.imread("images/image.jpg")
r,c = img.shape[:2]
print('r,c =', r, c)
new_img = cv2.resize(img, (2*c, 2*r), interpolation=cv2.INTER_CUBIC)
cv2.imwrite("images/resize_image.jpg", new_img)
cv2.imshow("resize", new_img)


cv2.waitKey(0)
cv2.destroyAllWindows()