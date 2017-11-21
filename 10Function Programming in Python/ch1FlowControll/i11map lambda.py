hello = lambda first, last: print("Hello", first, last)

bye = lambda first, last: print("Bye", first, last)

do_it = lambda f, *args: f(*args)


_ = list(map(do_it, [hello, bye], ['David', 'Jane'],
                ["Mertz", "Doe"]))