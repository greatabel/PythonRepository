#https://pypi.python.org/pypi/colorama

from colorama import Fore, Back, Style


def testA():
    items = ['a','b','c','d',1,2,3,4,5]
    
    for index, val in enumerate(items):
        print(index,val)
    print('让第一个为3，而不是0')
    for index, val in enumerate(items,3):
        print(index,val)



def main():
    print(Back.GREEN + 'and with a green background'+Back.RESET )
    
    print(Back.RED + 'and with a red background'+Back.RESET )
    testA()
    
    
    

            
if __name__ == '__main__':
    main()

