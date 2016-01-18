#http://dongweiming.github.io/blog/archives/guanyusignalyanjiu/
import signal
import os
import time


def receive_signal(signum, stack):#接收信号是通过建立一个回调函数，称为一个信号处理 ，信号发生时被调用
    print('Received:', signum)

if __name__ == "__main__":

    signal.signal(signal.SIGUSR1, receive_signal) 
    signal.signal(signal.SIGUSR2, receive_signal)
    print('My PID is:', os.getpid())
    while True:
        print('Waiting...')
        time.sleep(3) #每次暂停3秒钟。 当一个信号到来时，呼叫中断唤醒并用receive_signal做信号处理