import cv2
import numpy as np
img = cv2.imread("images/image.jpg")
ker = np.ones((5,5),np.uint8)
new_img = cv2.dilate(img,ker,iterations = 1)
# cv2.imwrite("dilation.jpg", new_img)
cv2.imshow("dilation", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()