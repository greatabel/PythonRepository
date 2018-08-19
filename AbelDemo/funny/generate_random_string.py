import string
import random

special_chs = "()`~!@#$%^&*-+=|{}[]:;'<>,.?/" 
characters = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_chs
 
digits = string.digits
def id_generator(size=6, chars=characters ):
    return ''.join(random.choice(chars) for _ in range(size))

print('30位数字字母', id_generator(30))
print('50位数字字母', id_generator(50))
print('digits(20纯数字)=', id_generator(20, digits))

print('-'*20)
for i in range(0, 5):
    print('20位数字字母:', id_generator(20))