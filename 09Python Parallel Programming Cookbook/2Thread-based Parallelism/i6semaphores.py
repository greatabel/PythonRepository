import threading
import time
import random

semaphore = threading.Semaphore(0)

if __name__ == '__main__':
    for i in range (5):
        print(i)