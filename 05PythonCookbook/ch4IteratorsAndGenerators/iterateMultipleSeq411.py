#https://pypi.python.org/pypi/colorama

from colorama import Fore, Back, Style




def main():
    print(Back.GREEN + 'my way'+Back.RESET )
    
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for i in range(0,min(len(xpts),len(ypts))):
        print(xpts[i],ypts[i])


    print(Back.RED + 'better way'+Back.RESET )
    for x, y in zip(xpts,ypts):
        print(x,y)

    print('other demo1--')
    a = [1, 2, 3]
    b = ['u','v','w', 'x', 'y', 'z']
    for i  in zip(a,b):
        print('i=',i)
    print('other demo2--')
    from itertools import zip_longest
    for i in zip_longest(a,b,fillvalue=0):
        print(i)

    print('demo3---')
    s = dict(zip(xpts,ypts))
    print(s)

    c = [10,20,30]
    for i in zip(a,b,c):
        print(i)
    print(list(zip(a,b,c)))


    
    
    

            
if __name__ == '__main__':
    main()

