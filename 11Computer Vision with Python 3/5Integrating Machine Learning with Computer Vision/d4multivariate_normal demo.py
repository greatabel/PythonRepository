# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.multivariate_normal.html
import numpy as np
import matplotlib.pyplot as plt


mean = [0, 0]
cov = [[1, 0], [0, 100]]  # diagonal covariance

#依据指定的均值和协方差生成数据
x, y = np.random.multivariate_normal(mean, cov, 500).T

print('x.shape, y.shape>', x.shape, y.shape)
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()

########################
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
v = np.vstack((a,b))
h = np.hstack((a,b))
print(a, '#', b, 'np.vstack((a,b)=\n', v,
        'np.hstack((a,b))=\n', h)

########################