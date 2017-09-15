from vec import Vec
from vecutil import zero_vec

label_list = ['a','b','c','d']
D = set(label_list)
rowlist = [Vec(D,{'a':4, 'b':-2,'c':0.5,'d':1}), Vec(D,{'b':2,'c':3,'d':3}),
               Vec(D,{'c':5, 'd':1}), Vec(D,{'d':2.})]
print('rowlist=', rowlist)
b = [6, -4, 3, -8]

def triangular_solve(rowlist, label_list, b):
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(D))):
        c = label_list[j]
        row = rowlist[j]
        print(b[j], x, row, row[c],'#'*20)
        x[c] = (b[j] - x*row)/row[c]
    return x

print(triangular_solve(rowlist, label_list, b))

