class Adder(object):
    def __init__(self, n):
        self.n = n

    def __call__(self, m):
        return self.n + m

def make_adder(n):

    def adder(m):
        return m + n

    return adder

add5_i = Adder(5)       # "instance" or "imperative”
add5_f = make_adder(5)
print('add5_i()=', add5_i(10), 'add5_f()=', add5_f(10))

add5_i.n = 10
print('add5_i()=', add5_i(10), 'add5_f()=', add5_f(10))