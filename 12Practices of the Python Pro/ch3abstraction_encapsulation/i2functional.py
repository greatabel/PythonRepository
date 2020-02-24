numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i * i)


from functools import reduce

# function style
square = map(lambda x: x * x, [1, 2, 3, 4, 5])
should = reduce(lambda x, y: x and y, [True, True, False])
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(square), should, list(evens))

from functools import partial

def pow(x, power=1):
    return x ** power


square = partial(pow, power=2)
cube = partial(pow, power=3)
print(square(10), cube(10))