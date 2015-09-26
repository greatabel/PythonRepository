from threading import Thread, Event
import time


def countdown(n, started_evt):
    print("countdown starting")
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(0.5)


started_evt = Event()

if __name__ == "__main__":
    print('Lauching countdown')
    t = Thread(target=countdown, args=(10, started_evt))
    t.start()

    started_evt.wait()
    print('countdown is running')