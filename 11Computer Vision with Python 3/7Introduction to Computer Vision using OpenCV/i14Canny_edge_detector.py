import cv2
img = cv2.imread("images/image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200, 3)
# cv2.imwrite("canny_edges.jpg", edges)
cv2.imshow("canny_edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()