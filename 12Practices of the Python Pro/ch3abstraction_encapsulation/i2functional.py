numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i * i)


from functools import reduce

# function style
square = map(lambda x: x * x, [1, 2, 3, 4, 5])
should = reduce(lambda x, y: x and y, [True, True, False])
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(square), should, list(evens))