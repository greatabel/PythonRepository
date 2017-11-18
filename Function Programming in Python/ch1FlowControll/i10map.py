def f1():
    return 1

def f2():
    return 2

def f3():
    return 3

do_it = lambda f, *args: f(*args)

r = map(do_it, [f1, f2, f3])
print(list(r))