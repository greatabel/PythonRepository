'''''''''
多线程版本：
5个线程各负责一个任务，全部完成最后只花了随机秒多一点时间，所以，对于阻塞性任务，例如IO密集型任务，
还是能发挥多线程的异步执行作用的，毕竟，时间花在IO等待上，如果是CPU密集型任务效果不大。
'''''''''
 
import time
import threading 
import random

'''
单独线程执行等耗时任务，使用sleeptime模拟耗时任务
'''
def  multiTask(t):
    print("thread:", t, "开始执行")
    sleeptime = random.randint(1, 5)
    time.sleep(sleeptime)
    print("thread:", t, "结束, 任务耗时", sleeptime,  " 秒钟")

'''
启动其他线程的主线程
'''
def main():
    threads = [threading.Thread(target = multiTask,args=(t,)) for t in range(0,10)]
    for t in threads:
        t.start()
 
    for t in threads:
        t.join()


if __name__ == '__main__':
    t1 = time.time()
    main()
    print("main thread 总共耗时:",round(time.time()-t1,2 ) ,"秒")
