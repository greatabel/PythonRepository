import threading
import time

def first_function():
    print (threading.currentThread().getName()+\
           str(' is Starting \n'))

def second_function():
    print (threading.currentThread().getName()+\
           str(' is Starting \n'))

if __name__ == "__main__":
    t1 = threading.Thread\
            (name='first_function', target=first_function)
    t2 = threading.Thread\
            (name='second_function', target=second_function)
    t1.start()
    t2.start()
    t1.join()
    t2.join()