import cv2
import numpy as np
from scipy.stats import itemfreq

# forest video from:
# https://www.youtube.com/watch?v=Lo6SpmjPwXo

debug_mode = True
# debug_mode = False

def get_dominant_color(image, n_colors):
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    flags, labels, centroids = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    palette = np.uint8(centroids)
    return palette[np.argmax(itemfreq(labels)[:, -1])]


def main():
    global debug_mode
    # cap = cv2.VideoCapture(0)


    font = cv2.FONT_HERSHEY_COMPLEX
    flag = 1

    global center
    if debug_mode:
        cap = cv2.VideoCapture("simulate.mov")
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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if flag == 0:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            l_h = cv2.getTrackbarPos("L-H", "Trackbars")
            l_s = cv2.getTrackbarPos("L-S", "Trackbars")
            l_v = cv2.getTrackbarPos("L-V", "Trackbars")
            u_h = cv2.getTrackbarPos("U-H", "Trackbars")
            u_s = cv2.getTrackbarPos("U-S", "Trackbars")
            u_v = cv2.getTrackbarPos("U-V", "Trackbars")

            lower_black = np.array([l_h, l_s, l_v])
            upper_black = np.array([u_h, u_s, u_v])

            mask = cv2.inRange(hsv, lower_black, upper_black)
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.dilate(mask, kernel)
            mask[np.where(mask == 0)] = 0
            # mask = cv2.Canny(mask,50,100)

            # Contours detection
            if int(cv2.__version__[0]) > 3:
                # Opencv 4.x.x
                contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            else:
                # Opencv 3.x.x
                _, contours, _ = cv2.findContours(
                    mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
                )
            oldArea = 0
            oldCnt = 0

            for cnt in contours:
                area = cv2.contourArea(cnt)
                approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
                diameter = np.sqrt(4 * area / np.pi)
                x = approx.ravel()[0]
                y = approx.ravel()[1]
                convvex = cv2.isContourConvex(cnt)
                # print(len(cnt))
                if cv2.arcLength(cnt, True) != 0:
                    circularity = (4 * np.pi * area) / (
                        (cv2.arcLength(cnt, True)) * (cv2.arcLength(cnt, True))
                    )

                if (
                    area > 500
                    and 0.5 <= float(circularity) <= 0.7
                    and 4 < len(approx) <= 7
                    and convvex == False
                ):

                    x1, y1, w1, h1 = cv2.boundingRect(cnt)

                    x2 = x1 + w1
                    y2 = y1 + h1
                    if x1 < 0:
                        x1 = 1
                    if y1 < 0:
                        y1 = 1
                    if x2 > 639:
                        x2 = 639
                    if y2 > 479:
                        y2 = 479
                    gray = gray[(y1):(y2), (x1):(x2)]
                    if gray.shape[0] != 0:
                        if gray.shape[1] != 0:
                            if y2 > y1:
                                if x2 > x1:
                                    """print(gray.shape)
                                    cv2.imshow("ngray", gray)"""
                                    rows = gray.shape[0]
                                    # cv2.imshow("daire",gray)
                                    circles = cv2.HoughCircles(
                                        gray,
                                        cv2.HOUGH_GRADIENT,
                                        1,
                                        rows / 8,
                                        param1=50,
                                        param2=15,
                                        minRadius=15,
                                        maxRadius=120,
                                    )
                                    if circles is not None:
                                        circles = np.uint16(np.around(circles))
                                        for i in circles[0, :]:
                                            center = (i[0] + x1, i[1] + y1)
                                            radius = i[2]

                                        if area >= oldArea:
                                            M = cv2.moments(cnt)
                                            cX = int(M["m10"] / M["m00"])
                                            cY = int(M["m01"] / M["m00"])
                                            if abs(center[0] - cX) < 40:
                                                
                                                cv2.drawContours(
                                                    frame, [approx], 0, (0, 0, 0), 5
                                                )
                                                cv2.line(
                                                    frame,
                                                    (cX, cY),
                                                    (cX, cY - 60),
                                                    (0, 255, 0),
                                                    thickness=2,
                                                )
                                                cv2.line(
                                                    frame,
                                                    (cX, cY),
                                                    (cX + 60, cY),
                                                    (255, 0, 0),
                                                    thickness=2,
                                                )
                                                cv2.line(
                                                    frame,
                                                    (cX, cY),
                                                    (cX - 30, cY + 30),
                                                    (0, 0, 255),
                                                    thickness=2,
                                                )
                                                cv2.putText(
                                                    frame,
                                                    "half round",
                                                    (x, y),
                                                    font,
                                                    1,
                                                    (100, 244, 237),
                                                    thickness=2,
                                                )
                                                oldArea = area
                                                oldCnt = cnt

        elif flag == 1:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img = cv2.medianBlur(gray, 37)
            circles = cv2.HoughCircles(
                img, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=40
            )

            if not circles is None:
                circles = np.uint16(np.around(circles))
                max_r, max_i = 0, 0
                for i in range(len(circles[:, :, 2][0])):
                    if circles[:, :, 2][0][i] > 50 and circles[:, :, 2][0][i] > max_r:
                        max_i = i
                        max_r = circles[:, :, 2][0][i]
                x, y, r = circles[:, :, :][0][max_i]
                if y > r and x > r:
                    square = frame[y - r : y + r, x - r : x + r]

                    dominant_color = get_dominant_color(square, 2)
                    if dominant_color[2] > 100:
                        print("detect half circle", dominant_color, "half above is #black")
                    elif dominant_color[0] > 80:
                        print("detect half circle", dominant_color, "half above is #white")

                    else:
                        print("detecting")

                for i in circles[0, :]:
                    cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)

        # 树梅派上可以注释掉下一行，不show出来
        if debug_mode:
            cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()