#encoding:utf-8

from colorama import Fore, Back, Style


def main():
    with open('sample2.txt', 'rb') as f: 
        data = f.read()
        print(data)
    # Write binary data to a file
    with open('sample2.txt', 'wb') as f: 
        f.write(b'Hello World')
    
    

            
if __name__ == '__main__':
    main()


