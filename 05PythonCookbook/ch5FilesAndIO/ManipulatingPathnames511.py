#encoding:utf-8
from colorama import Fore, Back, Style



def main():

    import os
    # print(os.getcwd())
    path = '/Users/abel/Downloads/AbelProject/PythonRepository/PythonCookbook/ch5FilesAndIO/sample.txt'
    print('os.path.basename(path)=',os.path.basename(path))
    print('os.path.dirname(path)=',os.path.dirname(path))
    print('join:',os.path.join('test1', 'test2', os.path.basename(path)))

    print(Fore.BLUE + "demo2:" + Style.RESET_ALL)
    print(Back.GREEN + 'Expand the user ''s home directory'+ Back.RESET)

    path = '~/t/test.csv'
    print('os.path.basename(path)=',os.path.basename(path))
    print('os.path.dirname(path)=',os.path.dirname(path))
    print(os.path.expanduser(path))
    print('split file extension',os.path.splitext(path))


            
if __name__ == '__main__':
    main()
