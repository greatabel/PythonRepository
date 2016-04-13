# Digit cancelling fractions
# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import time

def find_allmatches(numbers):
    results = []
    
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