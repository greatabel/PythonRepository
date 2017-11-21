from functools import reduce
from operator import mul


def factorialHOF(n):
    return reduce(mul, range(1, n+1), 1)

nhof = factorialHOF(5)
print("factorialHOF=", nhof)