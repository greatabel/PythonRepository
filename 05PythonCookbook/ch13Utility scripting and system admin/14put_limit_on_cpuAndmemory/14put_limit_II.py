import signal
import resource
import os

# def time_exceeded(signo, frame):
#     print("Time's up!")
#     raise SystemExit(1)

# def limit_memory(maxsize):
#     soft, hard = resource.getrlimit(resource.RUSAGE_SELF)
#     print('soft,hard',(soft,hard))
#     try:
#         resource.setrlimit(resource.RUSAGE_SELF, (10, 10))
#         soft, hard = resource.getrlimit(resource.RUSAGE_SELF)
#         print('soft,hard',(soft,hard))
#         return True

#     except ValueError:
#         return False
#     # signal.signal(signal.SIGUSR1, time_exceeded)

if __name__ == "__main__":

    resource.setrlimit(resource.RLIMIT_AS, (2048, 2048))
    x = list(range(100000))  # MemoryError! Make this 1000 to live on...
    print("limit not working!")
    print("Author said only work on linux but not osx")
        