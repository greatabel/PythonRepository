#sudo pip install pyserial
# -*- coding: utf-8 -*- 
from __future__ import print_function
import serial  
import time  

# 打开串口  "/dev/ttyAMA0", 9600 分别是串口名字和频率
ser = serial.Serial("/dev/ttyAMA0", 9600)

def main():  
    while True:  
        #  写数据过去
        ser.write("hello world")

        # 获得接收缓冲区字符  
        count = ser.inWaiting()  
        if count != 0:  
            # 读取内容并回显  
            recv = ser.read(count)  
            ser.write(recv)  
        # 清空接收缓冲区  
        ser.flushInput()  
        # 必要的软件延时  
        time.sleep(0.1)  
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  