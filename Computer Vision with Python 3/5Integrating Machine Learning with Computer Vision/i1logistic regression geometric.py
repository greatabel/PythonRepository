# https://florianhartl.com/logistic-regression-geometric-intuition.html

import sklearn.linear_model
# import sklearn.svm
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go

def np_r_demo():
    V = np.array([1,2,3,4,5,6 ])
    Y = np.array([7,8,9,10,11,12])
    C = np.r_[V[0:2],Y[0],V[3],Y[1:3],V[4:],Y[4:]]
    print(C)
# np_r_demo()

# data

np.random.seed(4)

X = np.r_[np.random.randn(20, 2), np.random.randn(20, 2) + [4, 4]]
# allows for graphs with width > height without distorting the aspect rati
X[:, 1] = X[:, 1] / 2.0

y = np.r_[np.zeros(20), np.ones(20)]
print(y)