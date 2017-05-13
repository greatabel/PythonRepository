import colorama
from colorama import Fore, Back, Style

    

def main():
    
    prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
    }
    print([n for n in prices if prices[n] >100])
    pos = (n for n in prices if prices[n] >100)
    print(pos)
    for x in pos:
        print("x=",x)
    print({key:value for key,value in prices.items() if value >100})


    iset = {'IBM','AAPL'}
    newDict = {key:value for key,value in prices.items() if key in iset }
    print('newDict=', newDict)

    #method2
    p1 = list((key, value) for key, value in prices.items() if value > 100)
    p2 = dict((key, value) for key, value in prices.items() if value > 100)

    print(p1, p2)


if __name__ == '__main__':
    main()
