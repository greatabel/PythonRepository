from threading import Thread
import time

class IOTask:
    def __init__(self):
        self._running = True
    def terminate(self):
        self._running = False
    def run(self, sock):
    # sock is a socket 
        # sock.settimeout(5) 
        while self._running:
        # Set timeout period
        # Perform a blocking I/O operation w/ timeout
            try:
                print('in try')
                # data = sock.recv(8192) 
                break
            except socket.timeout: 
                continue
                        # Continued processing
        # Terminated
        return

if __name__ == "__main__":
    c = IOTask()
    t = Thread(target=c.run, args=(10,))
    t.start()

    time.sleep(3)
    print('About to terminate')
    c.terminate()
    t.join()
    print('Terminated')