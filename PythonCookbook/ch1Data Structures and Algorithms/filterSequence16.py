import colorama
from colorama import Fore, Back, Style



def main():
    
    mylist = [1,-2,3,-4,5,-6]


    print(mylist)
    print(Fore.GREEN + "---" + Style.RESET_ALL)
    print([n for n in mylist if n >0])
    print([n for n in mylist if n <0])
    t = [n for n in mylist if n >0]
    print('t=',t)

    #迭代
    pos = (n for n in mylist if n > 0)
    print(pos)
    for x in pos:
        print("x=",x)

    values = ['1','2','test','N/A','-','3']
    #filter 函数
    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False

    ivals = list(filter(is_int, values))

    print('-'*30)
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
    print(addresses,counts)
    print(Fore.GREEN + ("-^-"*30) + Style.RESET_ALL)
    from itertools import compress
    more5 = [n > 5 for n in counts]
    print(list(compress(addresses, more5)))
    



if __name__ == '__main__':
    main()
