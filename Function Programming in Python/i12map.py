hello = lambda first, last: print("Hello", first, last)

bye = lambda first, last: print("Bye", first, last)

do_all_funcs = lambda fns, *args: [
    list(map(fn, *args)) for fn in fns]

_ = do_all_funcs([hello, bye],
                     ['David','Jane'], ['Mertz','Doe'])