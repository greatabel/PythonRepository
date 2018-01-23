import threading

shared_resource_with_lock  = 0
shared_resource_with_no_lock = 0
COUNT = 100000
shared_resource_lock = threading.Lock()

def increment_with_lock():
    print("increment_with_lock")

def decrement_with_lock():
    print("decrement_with_lock")


if __name__ == "__main__":
    t1 = threading.Thread(target = increment_with_lock)
    t2 = threading.Thread(target = decrement_with_lock)

    t1.start()
    t2.start()

    t1.join()
    t2.join()