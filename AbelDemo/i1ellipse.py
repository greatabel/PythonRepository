# http://www.cnblogs.com/cv-pr/p/4625122.html

from math import sin, cos, pi, sqrt
import numpy as np
from numpy.linalg import eig, inv
import matplotlib.pyplot as plt

import time
from termcolor import colored

# basis parameters of the ellipse
a = 8
b = 4

def ellipse(t, a, b):
    return a*cos(t), b*sin(t)

points = [ellipse(t, a, b) for t in np.linspace(0, 2*pi, 100)]
x, y = [np.array(v) for v in list(zip(*points))]
print('x,y ->', x, y, '#'*10, type(x), type(y))

def product_ellipse_test_data():
    return ""
# fig = plt.figure()
# plt.scatter(x, y)
# plt.show()

def fit_ellipse(x, y):
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    D =  np.column_stack((x**2, x*y, y**2, x, y, np.ones_like(x)))
    S = np.dot(D.T, D)
    C = np.zeros([6,6])
    C[0, 2] = C[2, 0] = 2
    C[1, 1] = -1
    E, V = eig(np.dot(inv(S), C))
    n = np.argmax(np.abs(E))
    return V[:, n]

tic = time.clock()
A, B, C, D, E, F = fit_ellipse(x, y)
K = D**2/(4*A) + E**2/(4*C) - F

# a, b
print('a:', sqrt(K/A), 'b:', sqrt(K/C))

toc = time.clock()
print(colored('time =>', 'red'),toc - tic)
