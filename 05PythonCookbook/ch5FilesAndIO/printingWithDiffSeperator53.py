#encoding:utf-8

from colorama import Fore, Back, Style


def main():
    print('ACME', 50, 91.5)
    print('ACME', 50, 91.5, sep=',')
    print('ACME', 50, 91.5, sep=',', end='!!\n')
    print(str.join(',',('ACME','50','91.5')))
    row = ('ACME', 50, 91.5)
    print(*row, sep=',')
    
    

            
if __name__ == '__main__':
    main()


