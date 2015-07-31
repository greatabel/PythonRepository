L1 = []
L2 = ["a","b","c"]
L3 = [ i * 10 for i in range(1,11)]

print(L1, L2, L3)

print('You can also use the built-in list type object to create lists:')
L4 = list()
L5 = list(range(10,20))
L6 = list(i * 2 for i in range(10,20))
print(L4, L5 ,L6)