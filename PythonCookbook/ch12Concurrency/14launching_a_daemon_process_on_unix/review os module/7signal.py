import signal


# Define signal handler function
def myHandler(signum, frame):
  print('I received: ', signum)

if __name__ == "__main__":
    #通过按下CTRL+Z向该进程发送SIGTSTP信号
    print(signal.SIGALRM)
    print(signal.SIGCONT)
    # register signal.SIGTSTP's handler 
    signal.signal(signal.SIGTSTP, myHandler)
    signal.pause()
    print('End of Signal Demo')