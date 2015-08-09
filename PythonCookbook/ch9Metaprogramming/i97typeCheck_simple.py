print(type([]) is list)
print(type({}) is dict)
print(type('') is str)
print(type(0) is int)

print('class type check:')
class Test1(object):
    pass
class Test2(Test1):
    pass

a = Test1()
b = Test2()

print(type(a) is Test1)
print(type(b) is Test2)