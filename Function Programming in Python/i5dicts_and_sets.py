print(' lists can be created in comprehensions rather than by ' +
    'creating an empty list, looping, and repeatedly calling .append() ')

a = {i: chr(65+i) for i in range(6)}
b = {chr(65+i) for i in range(6)}
print(a,b)