import cv2
import numpy as np
from scipy.stats import itemfreq

import pickle
import os

# forest video from:
# https://www.youtube.com/watch?v=Lo6SpmjPwXo

debug_mode = True

# 树梅派上可以关闭debug模式，不show出来，避免占用资源, 而且会读取连接树莓派上的桥接摄像头
# debug_mode = False

def get_dominant_color(image, n_colors):
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    flags, labels, centroids = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    palette = np.uint8(centroids)
    return palette[np.argmax(itemfreq(labels)[:, -1])]

def set_shared_object(area_rate):
    # --------- share data -------
    shared = {"area_rate": area_rate}
    fp = open("shared.pkl","wb")
    pickle.dump(shared, fp)
    # --------- share data end -------

def main():
    global debug_mode
    # cap = cv2.VideoCapture(0)
    index  = 0
    if debug_mode:
        cap = cv2.VideoCapture("simulate.mp4")
    else:
    # when use usb-camera ,only line you need to change is following:
        cap = cv2.VideoCapture(0)
        # cap = cv2.VideoCapture(-1)


    # Check if camera opened successfully
    if cap.isOpened() == False:
        print("Error opening video stream or file")

    # Read until video is completed
    while cap.isOpened():
        # while True:
        # ret, frame = cv2.VideoCapture('simulate.mov')
        ret, frame = cap.read()
        frame = cv2.GaussianBlur(frame, (5, 5), 0)


        ## convert to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        ## mask of green (36,25,25) ~ (86, 255,255)
        mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
        # mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

        ## slice the green
        imask = mask>0
        green = np.zeros_like(frame, np.uint8)
        green[imask] = frame[imask]

        # it make algorithm very slow, present not open it
        # dominant_color = get_dominant_color(hsv, 2)
        # print('dominant_color=', dominant_color)

        # circuluate rate
        green_perc = (mask>0).mean()
        print('green percentage in frame:', green_perc )

        if index % 10 == 0:
            print('index=', index)
            # we jump frame by 10 frames, to reduce circulation 
            set_shared_object(green_perc)
            
        # 树梅派上可以注释掉下一行，不show出来
        if debug_mode:
            cv2.imshow("Frame", green)
        index += 1
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()