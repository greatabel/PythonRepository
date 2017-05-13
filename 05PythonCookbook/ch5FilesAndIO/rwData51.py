#encoding:utf-8
#https://pypi.python.org/pypi/colorama
# 如果发现占用 ps aux | grep <string>
from colorama import Fore, Back, Style


def main():
    filepath = 'sample.txt'
    txt = open(filepath)
    print(txt.read())

    with open(filepath) as f:
        content = f.readlines()
        print('c=',content)

    with open(filepath) as f:
        lines = f.readlines()
        print(lines)

    with open(filepath, "r") as f:
        array = []
        for line in f:
            array.append(line)
            print('line=',line)
    
    with open(filepath,"wt") as f:
        f.write('test write')

    with open(filepath,"wt") as f:
        print("test",file=f)
        print("test1",file=f)
    #append
    with open(filepath,"a") as f:
        print("test2",file=f)
        print("test3",file=f)
        f.write("test4")
    
    
    

            
if __name__ == '__main__':
    main()


