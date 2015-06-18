#http://stackoverflow.com/questions/5890437/change-color-of-individual-print-line-in-python-3-2
# pip3 install colorama
import colorama
from colorama import Fore, Back, Style

colorama.init()

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(10)
d['b'].append(1)
print(d)

#输出彩色
text='test'
print(Fore.RED + text)
print(Back.GREEN + text + Style.RESET_ALL)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(1)
print(d)

d = {} # A regular dictionary 
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2) 
d.setdefault('b', []).append(4)
print(d)