adders = []
for n in range(5):
    adders.append(lambda m, n=n: m+n)

a1 = [adder(10) for adder in adders]
print(a1)

n = 10
a2 = [adder(10) for adder in adders]
print(a2)

add4 = adders[4]
print('add4(10, 100)=', add4(10, 100))