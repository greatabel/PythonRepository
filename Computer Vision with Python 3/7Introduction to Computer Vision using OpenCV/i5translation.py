import cv2
import numpy as np
img = cv2.imread("images/image.jpg")
r,c = img.shape[:2]
M = np.float32([[1,0,100],[0,1,100]])
new_img = cv2.warpAffine(img,M,(c,r))
cv2.imwrite("images/translation.jpg", new_img)
cv2.imshow("translation", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()