from threading import Thread

from time import sleep


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello from CookBook!"

    def print_message(self):
        print(self.message)

    def run(self):
        print("Thread starting\n")
        x = 0 
        while( x < 10):
            self.print_message()
            sleep(1)
            x += 1
        print("Thread Ended\n")

print("Main Process start")

hello_python = CookBook()

hello_python.start()

print("Main Process end.")