from collections import OrderedDict

import colorama
from colorama import Fore, Back, Style



def main():
    import random
    values = [10,20,30,40,50,60]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))

    print(random.sample(values,3))
    print(random.sample(values,3))
    print(random.sample(values,3))

    print(random.shuffle(values),values)
    print(random.shuffle(values),values)
    print(random.shuffle(values),values)


    print(Fore.GREEN + "more accurate" + Style.RESET_ALL)
    
    print("len bit",random.getrandbits(8))


if __name__ == '__main__':
    main()
