在树莓派/ubuntu18.04系统上测试过，windows应该可以，但是没测试过windows

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
打开一个命令行
模拟运行在:
python3 i1pi_car_detector.py

再开1个命令行分别进入虚拟环境，运行：
python3 i2receiver_with_cmd.py

可选：如果向查看模拟带ui的调用，还可以打开
python3 i3receiver_with_ui.py

6.
在真实创建下，不要打开i1pi_car_detector.py的UI，节省资源：
直接i1pi_car_detector.py的14行取消注释即可，取消debug模式


