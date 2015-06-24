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
    
    
    

            
if __name__ == '__main__':
    main()


