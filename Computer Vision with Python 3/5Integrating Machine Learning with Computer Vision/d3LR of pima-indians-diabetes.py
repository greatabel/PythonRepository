# http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data
from numpy import genfromtxt


dataset = genfromtxt('data/pima-indians-diabetes.data.csv', delimiter=',')
print(dataset.shape)
x = dataset[:, 0:7]
y = dataset[:, 8]