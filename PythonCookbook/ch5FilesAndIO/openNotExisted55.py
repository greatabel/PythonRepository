#encoding:utf-8

from colorama import Fore, Back, Style


def main():
    with open('sample3.txt', 'xt') as f: 
        f.write('test create')

    with open('sample3.txt','rt') as f1:
        content = f1.readlines()
        print(content)
    

            
if __name__ == '__main__':
    main()


