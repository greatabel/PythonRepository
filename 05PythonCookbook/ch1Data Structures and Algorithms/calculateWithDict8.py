

import colorama
from colorama import Fore, Back, Style

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}
def myway():
    minValue = 10000
    maxValue = 0
    minKey = ''
    maxKey = ''
    for key in prices:
        if prices[key] < minValue:
            minValue = prices[key] 
            minKey = key
        if prices[key] > maxValue:
            maxValue = prices[key]
            maxKey = key

    print(minKey,minValue)
    print(maxKey,maxValue)

def cleverWay():
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    print("min_price",min_price)
    print("max_price",max_price)
    prices_sorted = sorted(zip(prices.values(),prices.keys()))
    print("sorted:", prices_sorted)

def lambdaWay():
    print(min(prices, key = lambda k: prices[k]))
    print(prices[min(prices, key = lambda k: prices[k])])

def main():
    print(Fore.GREEN + "my pool way" + Style.RESET_ALL)
    myway()
    print(Fore.BLUE + "clever way --->" + Style.RESET_ALL)
    cleverWay()
    print(Fore.RED + "clever way --->" + Style.RESET_ALL)
    lambdaWay()




if __name__ == '__main__':
    main()