# import os

# def getch():
#     print("in getch")
#     os.system("bash -c \"read -n 1\"")
import os, platform
if platform.system() == "Windows":
    import msvcrt

def getch():
    print("#",platform.system())
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("bash -c \"read -n 1\"")
    elif platform.system() == "Windows":
        msvcrt.getch()


# print("Type a key!")
# getch()
# print("Okay")

if __name__ == '__main__':
    getch()