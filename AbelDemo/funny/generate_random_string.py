import string
import random
 
characters = string.ascii_uppercase + string.digits + string.ascii_lowercase
 
digits = string.digits
def id_generator(size=6, chars=characters ):
    return ''.join(random.choice(chars) for _ in range(size))

print('30位数字字母', id_generator(30))

print('50位数字字母', id_generator(50))
print('digits(20纯数字)=', id_generator(20, digits))