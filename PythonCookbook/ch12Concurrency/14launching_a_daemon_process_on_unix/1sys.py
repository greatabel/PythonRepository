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
    #http://stackoverflow.com/questions/14986490/python-change-sys-stdout-print-to-custom-print-function
    def print(*args, **kwargs):
        __builtins__.print("Custom--->", *args, **kwargs)
    print(x)
    print(100)

    for i in (sys.stdin, sys.stdout, sys.stderr):
        print(i)

    # output
    sys.stdout.write("Another way to do it!\n")
    x = input("read value via stdin: ")
    print("x=", x)

    # combine input and output
    while True:
        # output to stdout:
        print("###")
        try:

            number = input("Enter a nubmer:")
            print("number:", number)
            if not number:
                break
        except EOFError:
            print("\n here")
            break

    print("Coming through stdout")
    # stdout is saved
    save_stdout = sys.stdout

    fh = open("test.txt", "w")

    sys.stdout = fh
    print("This line goes to test.txt")

    # return to normal
    sys.stdout = save_stdout

    fh.close()




