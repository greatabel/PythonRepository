# deploy steps


1.
安装python3.6 以上版本

2. 
安装pip3 

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip 3install --upgrade -r requirements.txt

5.
一个terminal窗口执行监测的service端：
python3 i0simulate_camera_detect.py

另一个terminal窗口执行模拟接受的client：
python3 i1ros_read_from_detection.py


## 代码流程

# i0simulate_camera_detect.py

我们一开始参数化：parse_args() 决定是使用什么网络参数：是yolo3_darknet53
还是mobilenet的，可以使用不同的网络和参数（提前训练好，放在平级文件夹就行）
然后gpu决定是否使用GPU，还是cpu计算

image_put():
就是多进程里面读取视频的部分，如果是车载摄像头，直接打开里面的cap = cv2.VideoCapture(0)就可以


closest_colour() 是通过色域排除一些不需要监测的帧，通过对视频帧做一下主成分色彩分析


forked_version_cv_plot_bbox()： 这个是真正的监测模块，在里面监测到识别到类（买家训练的不止人的、头盔识别，就需要把自己多个类，比如茶几
，桌子，食物的各种想通知到client 的i1ros_read_from_detection 加入到 arning_signal 中），并且返回和瞄框。
然后还同步到python的缓存中

image_get() 是真正从视频/真实摄像头取帧程序，为了防止过载，提升小龙，我们默认为了方便展示程序开了窗口，
如果不想看到窗口，想静默，可以注释掉：
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow('image', orig_img[...,::-1])
这2行

run_single_camera() 就是读取什么摄像头：是车载的直接usb连过来的摄像头，还是从网络上的海康的枪击

# i1ros_read_from_detection.py
先引入各种tkinter依赖库，可以不需要，这是为了演示，所以专门做了UI

然后hello(): 就是保持读取python的pickle缓存部分 ，然后决定按照一定规律，不如连续读取到3个不同的object，然后决定放假的代码，可以放在这一个层级

__main__ : 部分主要就是UI的不绝和保持程序持续读取，这部分可以用ros的 service脚本替代掉
