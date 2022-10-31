在mac/ubuntu18.04系统上测试过，windows应该可以，但是没测试过windows

0.
安装rabbitmq server：
https://www.jianshu.com/p/5c8c4495827f

1.
安装python3.6 以上版本

2. 
安装pip3 
（如果网速慢 可以pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  把some-package替换成自己的慢的包 )

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
模拟运行在:
python3 wsgi.py

再开2个命令行分别进入虚拟环境，运行：
python3 i14simulate_iot.py
python3 i6more_attractive_gui.py

6.
浏览器访问：

http://localhost:5000/device_control
进行实验


7.
(可选功能：查看物联网主页和增删改查物联网设备)
已经注册好的账号 可以直接登录：
http://localhost:5000/home
username: greatabel1@126.com 
password: abel
你也可以自己注册和登录

