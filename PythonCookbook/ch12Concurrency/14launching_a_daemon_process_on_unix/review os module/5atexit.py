def goodbye(name, adjective):
    print('goodbye, %s, it was %s to meet you.' %(name, adjective) )

import atexit
atexit.register(goodbye,'Great','Abel')


# or
atexit.register(goodbye, adjective='who-send', name='Who-receive')