import cv2
import numpy as np


from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import math


# 读取彩色图片
image = cv2.imread("simulate.jpg")
output = image.copy()
# 将其转换为灰度图片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用hough变换进行圆检测
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    1,
    100,
    param1=100,
    param2=30,
    minRadius=100,
    maxRadius=200,
)
# 确保至少发现一个圆
if circles is not None:
    # 进行取整操作
    circles = np.round(circles[0, :]).astype("int")

    # 循环遍历所有的坐标和半径
    for (x, y, r) in circles:
        # 绘制结果
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # 显示结果
    cv2.imshow("output", np.hstack([image, output]))
    cv2.waitKey(0)


# # Create a VideoCapture object and read from input file
# # If the input is the camera, pass 0 instead of the video file name
# cap = cv2.VideoCapture('simulate.mov')

# # Check if camera opened successfully
# if (cap.isOpened()== False):
#   print("Error opening video stream or file")

# # Read until video is completed
# while(cap.isOpened()):
#   # Capture frame-by-frame
#   ret, frame = cap.read()
#   if ret == True:

#     # Display the resulting frame
#     cv2.imshow('Frame',frame)

#     # Press Q on keyboard to  exit
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#       break

#   # Break the loop
#   else:
#     break

# # When everything done, release the video capture object
# cap.release()

# # Closes all the frames
# cv2.destroyAllWindows()
