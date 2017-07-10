import time
from termcolor import colored

from math import gcd as bltin_gcd
# https://stackoverflow.com/questions/39678984/efficient-check-if-two-numbers-are-co-primes-relatively-primes
def coprime2(a, b):
    return bltin_gcd(a, b) == 1

# https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0
def main_process():

    for i in range(2, 10+1):
        count_cprime2 = 0
        for j in range(i):
            if coprime2(i, j+1):
                count_cprime2 += 1
                # print(i+1, j+1)
        print(i, '#', count_cprime2)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)