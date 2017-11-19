def hello1(name):
    print("Hello", name)

hello2 = lambda name: print("Hello", name)

hello1('David')
hello2('David')


print(hello1.__qualname__)
print(hello2.__qualname__)
hello3 = hello2
print(hello3.__qualname__)
hello3.__qualname__ = 'hello3'
print(hello3.__qualname__)
