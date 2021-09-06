import cv2
import numpy as np
from scipy.stats import itemfreq

# HC-SR04 超声波模块
#导入 GPIO库
import RPi.GPIO as GPIO
import time
  
#设置 GPIO 模式为 BCM
GPIO.setmode(GPIO.BCM)
  
#定义 GPIO 引脚
GPIO_TRIGGER = 23
GPIO_ECHO = 24
  
#设置 GPIO 的工作方式 (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


# debug模式是否开启，true就是开启
debug_mode = True
# debug_mode = False


def distance():
    # 发送高电平信号到 Trig 引脚
    GPIO.output(GPIO_TRIGGER, True)
  
    # 持续 10 us 
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
  
    start_time = time.time()
    stop_time = time.time()
  
    # 记录发送超声波的时刻1
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
  
    # 记录接收到返回超声波的时刻2
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
  
    # 计算超声波的往返时间 = 时刻2 - 时刻1
    time_elapsed = stop_time - start_time
    # 声波的速度为 343m/s， 转化为 34300cm/s。
    distance = (time_elapsed * 34300) / 2
  
    return distance


def hc_sr04():
    try:
        while True:
            dist = distance()
            print("Measured Distance = {:.2f} cm".format(dist))
            time.sleep(1)
            return dist
  
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

# -------

#这些是各个引脚的接口
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13
#GPIO初始化模式 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO初始化状态
def motor_init():
# pwm_ENA and pwm_ENB 是用来控制小车速度的
    global pwm_ENA 
    global pwm_ENB
    global delaytime #delaytime 可以用来控制小车的运动时间
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH) 
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #设置pwm频率
    pwm_ENA = GPIO.PWM(ENA,2000)
    pwm_ENB = GPIO.PWM(ENB,2000)
    #pwm启动
    pwm_ENA.start(0)
    pwm_ENB.start(0)

#############################################################################
#前面已经将小车的引脚初始化完成了，现在所需要的就是控制引脚的电流来控制小车的运动
#GPIO.output() 可以用来控制电流，pwm.ChangeDutyCycle()是用来控制频率的,间接用来控制车速
#我的小车的IN1和IN2是一对，IN3和IN4是一对 当1是HIGH的时候左边前进,2是HIGH的时候左边后退
#1和2，3和4 只能是HIGH和LOW 一对的 不能是两个都是HIGH 或者 LOW
#可能每个人的车都不一样吧，大体套路都是一样的
############################################################################
#前进
def run(delaytime):
    GPIO.output(IN1,GPIO.HIGH)  #setting GPIO
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80) #setting speed
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime) #setting delaytime
#左转
def left(delaytime):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(40)
    pwm_ENB.ChangeDutyCycle(40)
    time.sleep(delaytime)
#原地左转
def spin_left(delaytime):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(10)
    pwm_ENB.ChangeDutyCycle(40)
    time.sleep(delaytime)

def right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)
#原地右转
def spin_right(delaytime):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)
#停车
def brake(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)
#后退
def back(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(80)
    pwm_ENB.ChangeDutyCycle(80)
    time.sleep(delaytime)

# ------

# 获取分析的image的数组的主要颜色成分
def get_dominant_color(image, n_colors):
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    flags, labels, centroids = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    palette = np.uint8(centroids)
    return palette[np.argmax(itemfreq(labels)[:, -1])]


# 主函数
def main():
    global debug_mode
    # cap = cv2.VideoCapture(0)

    # 向前跑138cm
    run(138)
    # 向左转
    spin_left(1)

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
    # 检查摄像头是否正常运转
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

            # 获取黑色-红色色域的上下界限
            lower_black = np.array([l_h, l_s, l_v])
            upper_black = np.array([u_h, u_s, u_v])

            # 转化成这遮罩，应用到图上
            mask = cv2.inRange(hsv, lower_black, upper_black)
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.dilate(mask, kernel)
            mask[np.where(mask == 0)] = 0
            # mask = cv2.Canny(mask,50,100)

            #根据opencv 3和4 ，进行兼容
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
                # 根据监测到的色块大小进行过滤，排除噪音部分
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
                                    # 获得检测到的圆形
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
                        # 发现路标的上半部分是黑色
                        print("detect half circle", dominant_color, "half above is #black")
                        # 黑色的情况，想左转，直行
                        spin_left(1)
                        if hc_sr04() == 10:
                            spin_left(1)
                            run(20)

                    elif dominant_color[0] > 80:
                        # 发行路标的上半部分是非黑色（因为路标只有一半黑一半白，那就是白色）
                        print("detect half circle", dominant_color, "half above is #white")
                        # 如果是白色，前进小段(随机)，右转
                        run(random.int(0,5))
                        spin_right(1)
                        if hc_sr04() == 10:
                            
                            spin_left(random.int(0,5))                        
                    else:
                        print("detecting")
                # 对帧进行圆形图案增加周边的色框
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