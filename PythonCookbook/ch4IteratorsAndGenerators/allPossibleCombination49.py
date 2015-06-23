#https://pypi.python.org/pypi/colorama

from colorama import Fore, Back, Style


def dullway_fullCombination():
    items = ['a','b','c']
    index = 0
    for item1 in items:
        for item2 in items:
            for item3 in items:
                print(item1,item2,item3)
                index += 1
    print('index=',index)

def dullway():
    items = ['a','b','c']
    index = 0
    for item1 in items:
        for item2 in items:
            for item3 in items:
                if item1!=item2 and item1!=item3 and item2!=item3:
                    print(item1,item2,item3)
                    index += 1
    print('index=',index)

def cookbookway():
    items = ['a','b','c']
    from itertools import permutations
    for p in permutations(items):
        print(p)


def main():
    print(Back.GREEN + 'and with a green background'+Back.RESET )
    
    dullway_fullCombination()
    print(Back.YELLOW + 'and with a green background'+Back.RESET )
    dullway()
    print(Back.RED + 'and with a red background'+Back.RESET )
    cookbookway()
    
    
    
    

            
if __name__ == '__main__':
    main()

