# http://www.python-course.eu/sys_module.php
import sys

if __name__ == '__main__':
    print(sys.version)
    print('-' * 10)
    # print(help(sys))

    # it's easy to print this list 
    print(sys.argv)
    for i in range(len(sys.argv)):
        if i == 0:
            print("Function name: %s" % sys.argv[0])
        else:
            print("%d. argument: %s" % (i,sys.argv[i]) )

    # change the output behaviour
    x = 42
    print(x)
    def print(*args, **kwargs):
        __builtins__.print("Custom--->", *args, **kwargs)
    print(x)
    print(100)