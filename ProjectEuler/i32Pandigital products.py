# Pandigital products
# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import time
import math

def isPandigital(string):
    thelen = len(string)
    # print(string,'thelen=', thelen)
    for i in range(1, thelen+1):
        # print('str(i)=', str(i))
        if str(i) not in string:
            return False
    if thelen > 9:
        return False
    return True

def find_allmatches(numbers):
    print(numbers)
    for i in range(0, int(math.pow(10,3))):
        if isPandigital(str(i)):
            print(i)



if __name__ == "__main__":
    tic = time.clock()
    # for i in range(0,20):
    #     print(i,fib(i),len(str(fib(i))))
    # find_allpowers(5,5)
    # find_allpowers(10000,4)
    results = find_allmatches(list(range(1,10)))
    print('#', results)

    toc = time.clock()
    print("time=",toc - tic)