import colorama
from colorama import Fore, Back, Style

words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]

def myway():
    mydict ={}
    for item in words:
        if item in mydict:
            mydict[item] += 1
        else:
            mydict[item] = 1
    mymax = max(zip(mydict.values(), mydict.keys()))
    print(mymax)




def betterWay():
    from collections import Counter
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)


def main():
    colorama.init()
    text='test'
    print(Fore.RED + "my way" + Style.RESET_ALL)
    myway()
    print(Fore.BLUE + "better way" + Style.RESET_ALL)
    betterWay()


if __name__ == '__main__':
    main()

