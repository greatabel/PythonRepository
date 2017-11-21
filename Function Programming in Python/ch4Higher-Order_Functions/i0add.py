from functools import reduce


add5 = lambda n: n+5
t = reduce(lambda l, x: l+[add5(x)], range(10), [])
print(t)