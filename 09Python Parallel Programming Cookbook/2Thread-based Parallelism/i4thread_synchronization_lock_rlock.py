import threading

shared_resource_with_lock  = 0
shared_resource_with_no_lock = 0
COUNT = 100000
shared_resource_lock = threading.Lock()

def increment_with_lock():
    print("increment_with_lock")

def decrement_with_lock():
    print("decrement_with_lock")

def increment_without_lock():
    print("### increment_without_lock")

 
def decrement_without_lock():
    print("@@@ decrement_without_lock")

if __name__ == "__main__":
    t1 = threading.Thread(target = increment_with_lock)
    t2 = threading.Thread(target = decrement_with_lock)
    t3 = threading.Thread(target = increment_without_lock)
    t4 = threading.Thread(target = decrement_without_lock)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()