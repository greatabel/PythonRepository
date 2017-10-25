# http://www.cnblogs.com/cv-pr/p/4625122.html

from math import sin, cos, pi, sqrt, atan
import numpy as np
from numpy.linalg import eig, inv
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Ellipse

# from scipy.optimize import fsolve

import time
from termcolor import colored


def ellipse(t, a, b):
    # return a*cos(t), b*sin(t)
    a1 = a*cos(t)
    b1 = b*sin(t)
    a2 = a1*cos(pi * 5/6)-b1*sin(pi*5/6)
    b2 = b1*cos(pi*5/6)+a1*sin(pi*5/6)
    r = sqrt(a2 ** 2 + b2 ** 2)
    angle = atan(b2 / a2)
    # if a2 < 0:
    #     angle += pi
    # if a2 > 0 and b2 < 0:
    #     angle += 2*pi

    print('#'*5, 'angle=',angle*180/pi, 'r=',r, 'a2=', a2, 'b2=',b2)
    # return a1*cos(pi/2)-b1*sin(pi/2),b1*cos(pi/2)+a1*sin(pi/2)
    # return a1*cos(pi/3)-b1*sin(pi/3),b1*cos(pi/3)+a1*sin(pi/3)
    return a2, b2

def product_ellipse_test_data(a, b, data_count):
    points = [ellipse(t, a, b) for t in np.linspace(0, 2*pi, data_count)]
    print('points->', points)
    # points = [(10.0, 0.0), (-3.2999999999999985, 5.7157676649772959),
    #  (-3.3000000000000029, -5.7157676649772933)]
    x, y = [np.array(v) for v in list(zip(*points))]
    # print(x[1],x[2], y[1], y[2], '#'*10, type(x), type(y))
    noise = np.random.rand(data_count)/10
    x += noise
    y += noise
    # print('noise->', noise)
    print('#'*10,'type(x)=' ,type(x),type(y), x, y)
    return x, y

def fit_ellipse(x, y):
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    # build design matrix
    D =  np.column_stack((x**2, x*y, y**2, x, y, np.ones_like(x)))
    # build scatter matrix
    S = np.dot(D.T, D)
    # build 6x6 constraint matrix
    C = np.zeros([6,6])
    C[0, 2] = 2
    C[2, 0] = 2
    C[1, 1] = -1
    # solve eigensystem
    E, V = eig(np.dot(inv(S), C))
    # find the positive eigenvalue
    n = np.argmax(np.abs(E))

    return V[:, n]

def fit_ellipse_simplify(x, y):
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    # build design matrix
    D =  np.column_stack((x**2, x*y, y**2, np.ones_like(x)))
    # build scatter matrix
    S = np.dot(D.T, D)
    # build 6x6 constraint matrix
    C = np.zeros([4,4])
    C[0, 2] = 2
    C[2, 0] = 2
    C[1, 1] = -1
    # solve eigensystem
    E, V = eig(np.dot(inv(S), C))
    # find the positive eigenvalue
    n = np.argmax(np.abs(E))

    return V[:, n]

def caculate(A, B, C, D ,E ,F):
    t1 = 2 * (B**2 - 4 * A * C) * F
    t2 = sqrt((A - C)**2 + B ** 2)
    t3 = B**2 - 4 * A * C
    a = -1*sqrt(t1 * (A + C + t2)) / t3
    b = -1*sqrt(t1 * (A + C - t2)) / t3

    angle = atan( (C - A - t2)/ B )
    return a, b, angle

if __name__ == '__main__':
    x, y = product_ellipse_test_data(10, 5, 8)
    print('test data->', x, y)

    # print(x[1],x[2], y[1], y[2],'#'*20)
    tic = time.clock()
    A, B, C, D, E, F = fit_ellipse(x, y)
    # A, B, C, D, E, F = A/F, B/F, C/F, D/F, E/F, 1
    print(' A, B, C, D, E, F->',  A, B, C, D, E, F)
    i1,i2,i3,i4 = fit_ellipse_simplify(x, y)
    # i1,i2,i3,i4 = i1/i4,i2/i4,i3/i4,i4/i4
    print(colored('##', 'red'),'i1,i2,i3,i4 ->',  i1,i2,i3,i4)

    a, b , angle = caculate(i1, i2, i3, 0, 0, i4)
    # a, b , angle = caculate(A, B, C, D, E, F)
    print('a,b, angle->', a, b, angle,angle *180/pi)
    # def func(i):
    #         a, b, t = i[0], i[1], i[2]
    #         return (
    #                 (a * t) ** 2 + b**2 *(1- t ** 2)  - 4,
    #                 4 *(b**2 - a**2)**2 * (t**2)*(1- t**2) ,
    #                 a**2 * (1 - t ** 2) + (b * t)**2 - 9
    #                )
    # r = fsolve(func,[0,0,0])
    # print('#'*10, r)

    # K = D**2/(4*A) + E**2/(4*C) - F
    # a = sqrt(K/A)
    # b = sqrt(K/C)
    # print('a:',a, 'b:', b)

    # toc = time.clock()
    # print(colored('time =>', 'red'), toc - tic, colored('seconds', 'red'))
    # # fig = plt.figure()
    # # plt.scatter(x, y)
    # # plt.show()
    # fig = plt.figure()
    # # plt.scatter(x, y)
    # # plt.show()
    ax = plt.subplot(111, aspect='equal')

    ell = Ellipse(xy=(0,0),
                  width=a*2, height=b*2, angle=angle *180/pi,
                  edgecolor='r', fc='None', lw=2
                  )
    ell.set_facecolor('none')
    ax.add_artist(ell)

    plt.scatter(x, y)
    plt.show()




