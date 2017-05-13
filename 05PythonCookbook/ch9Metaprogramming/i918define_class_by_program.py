def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def __repr__(self):
    return '## {0}, {1}, {2} #!'.format(self.name, self.shares, self.price)

def cost(self):
    return self.shares * self.price

cls_dict = {
    '__init__': __init__,
    '__repr__': __repr__,
    'cost':cost,
}

import types

Stock = types.new_class('Stock',(), {}, lambda ns: ns.update(cls_dict))

if __name__ == '__main__':
    s = Stock('APPLE', 100,9)
    print(s)
    print('s.cost=',s.cost())