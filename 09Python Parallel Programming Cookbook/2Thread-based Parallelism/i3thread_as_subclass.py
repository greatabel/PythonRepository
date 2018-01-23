import threading
import time


exit_Flag = 0

def print_time(threadName, delay, counter):
    print('exit_Flag=', exit_Flag, '#'*10)
    while counter:
        if exit_Flag:
            thread.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time()) ))
        counter -= 1

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("Starting " + self.name + "\n")
        print_time(self.name, self.counter, 5)
        print ("Exiting " + self.name + "\n")


if __name__ == "__main__":
    print("Start Main Thread")
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exiting Main Thread")
