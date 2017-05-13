import colorama
from colorama import Fore, Back, Style




def main():
    items = [1,20,300,4000]
    print("demo1 --- items ",items)
    #https://docs.python.org/3/howto/functional.html
    it = iter(items)
    print(tuple(it))

    it = iter(items)
    print(list(it))

    it = iter(items)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))


    # print(next(it)) # 会导致出错
    print(Fore.GREEN + "demo2:" + Style.RESET_ALL)
    M = [[1,2,3],[10,20,30],[100,200,300]]
    G = (sum(row) for row in M) # create a generator of row sums
    print(next(G))
    print(next(G))
    print(next(G))

            
if __name__ == '__main__':
    main()

