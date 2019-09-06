'''

Python中如何实现多线程？

#----------------------------#



'''
import logging
import threading
import time
from termcolor import colored


def thread_function(name):
    logging.info("线程 %s: starting", name)
    time.sleep(2)
    logging.info("线程 %s: finishing", name)



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("主线程    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("主线程    : before running thread")
    x.start()
    logging.info("主线程    : wait for the thread to finish")
    # x.join()
    logging.info("主线程    : all done")





