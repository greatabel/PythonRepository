from vec import Vec


label_list = ['a','b','c','d']
D = set(label_list)
rowlist = [Vec(D,{'a':4, 'b':-2,'c':0.5,'d':1}), Vec(D,{'b':2,'c':3,'d':3}),
               Vec(D,{'c':5, 'd':1}), Vec(D,{'d':2.})]
print(rowlist)