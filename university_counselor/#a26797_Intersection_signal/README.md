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
python3 i2improved_version.py





# ------ 总需求 ------

1.
买家的“亦庄1.0的开源数据”用不上，我们自己模拟路口或者用开源数据接入（如果能找到合适的中国数据集或者开源过滤出中国）

2.
模拟交叉口数量和布局：确定研究区域内的交叉口数量和布局情况，并将其用数字或图形进行表达；
模拟交通流量和车速：根据实际情况或假设的交通流量和车速，为每个交叉口设置车辆到达时间和车辆通过时间等参数。

3.
编写交叉口协调算法：选择合适的交叉口协调算法，如红绿灯配时算法、自适应交通信号控制算法等

4.
捣鼓仿真分析：通过运行numpy编写的算法，进行交通仿真分析，观察交通流量、车速、等待时间、拥堵情况等指标的变化

5.
增加机器学习部分（具体怎么加需要看模拟实验的情况）

6.
写2页开题报告


# ------ end 总需求 ------





