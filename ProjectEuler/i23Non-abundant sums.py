
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def divisorGenerator(n):
    # print("divisorGenerator ",n)
    for i in range(1,int(n/2)+1):
        if n%i == 0: 
            # print(i)
            yield i

def  find_abundant_below_num(num):
    mydict = {}
    for number in range(1,num):
        thesum = sum(list(divisorGenerator(number)))
        print("sum=",thesum)
        if thesum > number:
            mydict[number] = 1
        else:
            mydict[number] = 0
    # print(mydict)
    return mydict

if __name__ == "__main__":
    find_abundant_below_num(30)