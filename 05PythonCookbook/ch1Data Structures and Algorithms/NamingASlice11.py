import colorama
from colorama import Fore, Back, Style

record = '....................100          .......513.25     ..........'
def myway():
    cost = int(record[20:32]) * float(record[40:48])
    print(cost)




def betterWay():
    SHARES = slice(20,32)
    PRICE  = slice(40,48)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)


def main():
    colorama.init()
    text='test'
    print(Fore.RED + "my way" + Style.RESET_ALL)
    myway()
    print(Fore.BLUE + "better way" + Style.RESET_ALL)
    betterWay()


if __name__ == '__main__':
    main()