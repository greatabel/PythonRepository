# https://lz5z.com/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%B8%B8%E7%94%A8%E7%AE%97%E6%B3%95%E2%80%94%E9%80%BB%E8%BE%91%E5%9B%9E%E5%BD%92/
# http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data
from numpy import genfromtxt

from sklearn import preprocessing
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


dataset = genfromtxt('data/pima-indians-diabetes.data.csv', delimiter=',')

print(dataset.shape)
x = dataset[:, 0:7]
y = dataset[:, 8]

print('len(x), x[0:10] >', len(x), x[0:3])

# 数据归一化是指把数字变成（0,1）之间的小数。
normalized_X = preprocessing.normalize(x)
print('len(normalized_X), normalized_X[0:10] >', len(normalized_X), normalized_X[0:3])

# 逻辑回归
model = LogisticRegression()

model.fit(normalized_X, y)

# 预测
expected = y
predicted = model.predict(normalized_X)

print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))