import grok

print("I'am i3spam.py")

print('解决方案：http://stackoverflow.com/questions/1054271/how-to-import-a-python-class-that-is-in-a-directory-above')
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import B.bar
