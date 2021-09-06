
1.
安装python3.6 以上版本

2. 
安装pip3 

如果是osx/linux，可以跳过 步骤3，4，因为我已经打包了虚拟环境,
虚拟环境在wsgi.py平行的目录的 mlsystem-env

3.
可选（创建python3虚拟环境，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

create virtual environment:
python3 -m venv  mlsystem-env


4.
(如果进行了步骤3， 就进入虚拟环境，执行后面的，没有就直接执行4)
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt

5.
命令行进入wsgi.py平行的目录目录,执行下列命令，进入虚拟环境
then enter virtual environment:
Windows run:
mlsystem-env\Scripts\activate.bat

Unix/MacOS run:
source mlsystem-env/bin/activate


6.
在虚拟环境中，命令行进入wsgi.py平行的目录目录，执行：
python3 i2pi_car_advanced.py

7.
在生产环境上可以关闭debug模式：
打开debug_mode = False
的注释即可，将会读取真实摄像头（不过你得实验下是index=-1还是0）
而且关闭窗口显示，减少资源占用