a = float(input("What is your a? "))
b = float(input("What is your b? "))

sm  = a + b
sub = a - b
pro = a * b
quo = a / b
re  = a % b
import math
lg  = math.log(a, 10)
rs  = pow(a, b)

print("sum: %.2f sub: %.2f pro:%.2f quo:%.2f re:%.2f log10a: %.2f power:%.2f" % (sm, sub, pro ,quo,re,lg,rs))