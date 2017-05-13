from _thread import start_new_thread

def heron(a):
    """Calculates the square root of a"""
    eps = 0.0000001
    old = 1
    new = 1
    while True:
        old,new = new, (new + a/new) / 2.0
        print(old, new)
        if abs(new - old) < eps:
            break
    return new

if __name__ == "__main__":
    start_new_thread(heron, (99,))
    start_new_thread(heron, (999,))
    # import time
    # time.sleep(3)
    # another way is:
    # c = input("type something to quit.")
