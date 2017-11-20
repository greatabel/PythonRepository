import functools, operator

class Math(object):
    def product(*nums):
        return functools.reduce(operator.mul, nums)

    def power_chain(*nums):
        return functools.reduce(operator.pow, nums)

    def abel_print():
        print("test print")

ph = Math.product(3, 4, 5)
pw = Math.power_chain(3, 4, 5)
print(ph, pw)
Math.abel_print()