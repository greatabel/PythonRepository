numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i * i)


from functools import reduce


square = map(lambda x: x * x, [1, 2, 3, 4, 5])
print(list(square))