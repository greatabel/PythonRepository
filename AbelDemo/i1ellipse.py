# http://www.cnblogs.com/cv-pr/p/4625122.html

from math import sin, cos, pi, sqrt
import numpy as np
from numpy.linalg import eig, inv
import matplotlib.pyplot as plt

import time
from termcolor import colored

# basis parameters of the ellipse


def ellipse(t, a, b):
    return a*cos(t), b*sin(t)


def product_ellipse_test_data(a, b, data_count):

    points = [ellipse(t, a, b) for t in np.linspace(0, 2*pi, data_count)]
    x, y = [np.array(v) for v in list(zip(*points))]
    # print(x[1],x[2], y[1], y[2], '#'*10, type(x), type(y))
    noise = np.random.rand(data_count)
    x += noise
    y += noise
    # fig = plt.figure()
    plt.scatter(x, y)
    plt.show()
    print('noise->', noise)
    return x, y




def fit_ellipse(x, y):
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    D =  np.column_stack((x**2, x*y, y**2, x, y, np.ones_like(x)))
    S = np.dot(D.T, D)
    C = np.zeros([6,6])
    C[0, 2] = 2
    C[2, 0] = 2
    C[1, 1] = -1
    E, V = eig(np.dot(inv(S), C))
    n = np.argmax(np.abs(E))
    return V[:, n]

if __name__ == '__main__':
    x, y = product_ellipse_test_data(8, 4, 8)
    print(x[1],x[2], y[1], y[2],'#'*20)
    tic = time.clock()
    A, B, C, D, E, F = fit_ellipse(x, y)
    K = D**2/(4*A) + E**2/(4*C) - F

    # a, b
    print('a:', sqrt(K/A), 'b:', sqrt(K/C))

    toc = time.clock()
    print(colored('time =>', 'red'),toc - tic)
