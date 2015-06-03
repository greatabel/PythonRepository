# -*- coding: utf-8 -*-

"""
source from http://segmentfault.com/a/1190000000641920
""" 
try:
    import cPickle as pickle
except:
    import pickle
import pprint

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print('DATA:'),
pprint.pprint(data)

data_string = pickle.dumps(data)
print('PICKLE:'),
pprint.pprint(data_string)

data2 = pickle.loads(data_string)
print('AFTER:'),
pprint.pprint(data2)

print('SAME?:', (data is data2))
print('EQUAL?:', (data == data2))