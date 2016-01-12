import os

if __name__ == "__main__":
    command = " "
    while  command != "exit":
        command = input("command:")
        handle = os.popen(command)
        line = " "
        while line:
            line = handle.read()
            print(line)
        handle.close()
    print("that is it!")