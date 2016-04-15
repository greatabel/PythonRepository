# Digit factorials
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import time

def get_digital(number):
    results = []
    while number > 0:
        result = number % 10
        number = number // 10
        results.append(result)
    # print('results=', results)
    return results

def factorial_sum(num):
    results = get_digital(num)
    # print('results1=', results)
    mysum = 0
    for d in results:
        # print('d=', d)
        temp = 1
        for i in range(1, d+1):
            # print("i=", i)
            temp *= i
        # print('temp=', temp)
        mysum += temp
    return mysum

def find_possible_limit():
    flag = True
    for i in range(1,20):
        assume = 10**i - 1
        factor = factorial_sum(assume)
        print(i,' assume=', assume, factor)
        if assume > factor:
            print('possible limit digits length:',i)
            return i
        
    return -1





if __name__ == "__main__":
    tic = time.clock()
    limit = find_possible_limit()
    mysum = 0
    for i in range(3, 10**limit):
        if factorial_sum(i) == i:
            print(i)
            mysum += i
        if i % 10000 == 0:
            print("i=", i)
    print('mysum = ', mysum)


    toc = time.clock()
    print("time=",toc - tic)