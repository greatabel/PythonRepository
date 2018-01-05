import string
import random
 
characters = string.ascii_uppercase + string.digits + string.ascii_lowercase
 
def id_generator(size=6, chars=characters ):
    return ''.join(random.choice(chars) for _ in range(size))

print(id_generator(30))