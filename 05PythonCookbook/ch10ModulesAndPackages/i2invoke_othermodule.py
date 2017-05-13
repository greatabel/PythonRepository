from i2controll_import_of_everythiing.somemodule import *

import sys

if __name__ == "__main__":
    spam()
    grok()
    try:
        test()
    except:
        print("#unexpected errors:", sys.exc_info()[0])

    try:
        print(blah)
    except:
        print("@unexpected errors:", sys.exc_info()[0])

