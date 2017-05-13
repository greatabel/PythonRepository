import traceback
import sys

def func(n): 
    return n + 10

try: 
    func('N/A')
except:
    print('**** AN ERROR OCCURRED ****')
    traceback.print_exc(file=sys.stderr)