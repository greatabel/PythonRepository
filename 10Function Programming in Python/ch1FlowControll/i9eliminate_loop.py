def func(e):
    return e * 10

it = list(range(5))

print('# statement-based loop')
for e in it:
    r = func(e)
    print(r)

print('# map()-based "loop"')
t = list(map(func, it))
print(t)