# Consider quadratic Diophantine equations of the form:

# x2 – Dy2 = 1

# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

# It can be assumed that there are no solutions in positive integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

# 32 – 2×22 = 1
# 22 – 3×12 = 1
# 92 – 5×42 = 1
# 52 – 6×22 = 1
# 82 – 7×32 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


import time
from termcolor import colored

def the_fomula(x,y,d):
    return x**2 - d * y**2 - 1 == 0

def main_process():
    for i in range(2,7+1):
        print("D=",i)
        for j in range(1,10):
            for k in range(1,10):
                if the_fomula(j,k,i):
                    print(j,k,i)
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)