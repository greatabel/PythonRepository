import colorama
from colorama import Fore, Back, Style

class Countdown:
    #http://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do  
    #  __init__ 的作用
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n*100 #show more strange
            n += 1


def main():
    c = Countdown(5)
    print(list(c))
    print(Fore.GREEN + "more accurate" + Style.RESET_ALL)
    print(list(reversed(c)))

if __name__ == '__main__':
    main()

