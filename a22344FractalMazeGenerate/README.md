
1.
安装python3.6 以上版本

2. 
安装pip3 



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
