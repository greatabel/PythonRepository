#encoding:utf-8
from colorama import Fore, Back, Style



def main():

    import os
    print(os.path.exists('/Users/abel'))
    myfile = '/Users/abel/Downloads/AbelProject/PythonRepository/PythonCookbook/ch5FilesAndIO/sample.txt'
    print(os.path.isfile(myfile))

    print(Fore.BLUE + "demo2:" + Style.RESET_ALL)
    print(Back.GREEN + 'Expand the user ''s home directory'+ Back.RESET)

    print(os.path.isfile(myfile))
    print(os.path.getsize(myfile))
    import time
    print(time.ctime(os.path.getatime(myfile)))




            
if __name__ == '__main__':
    main()
