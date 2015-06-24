#https://pypi.python.org/pypi/colorama
# 如果发现占用 ps aux | grep <string>
from colorama import Fore, Back, Style


def main():
    print(Back.GREEN + 'my way'+Back.RESET )
    
    import sys
    f = open('passwd.txt')
    for chunk in iter(lambda: f.read(10), ''):
        n = sys.stdout.write(chunk)
        print('\n-->')


    
    
    

            
if __name__ == '__main__':
    main()

