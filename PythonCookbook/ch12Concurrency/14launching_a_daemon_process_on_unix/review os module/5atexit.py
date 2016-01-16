# https://docs.python.org/3/library/atexit.html

import atexit

def goodbye(name, adjective):
    print('goodbye, %s, it was %s to meet you.' %(name, adjective) )

@atexit.register
def test2():
    print("In test2!")



atexit.register(goodbye,'Great','Abel')
# or
atexit.register(goodbye, adjective='who-send', name='Who-receive')