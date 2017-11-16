import cv2
s_img = cv2.imread("sns/M0BGDK15000901T3KXSF61TM9f675.jpg")
l_img = cv2.imread("sns/bg.jpg")
x_offset=130
y_offset=210
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

cv2.imwrite("sns/test.jpg", l_img)
cv2.imshow("l_img", l_img)


cv2.waitKey(0)
cv2.destroyAllWindows()