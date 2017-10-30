import numpy as np
import matplotlib.pyplot as plt


mean = [0, 0]
cov = [[1, 0], [0, 100]]  # diagonal covariance


x, y = np.random.multivariate_normal(mean, cov, 500).T
print(x,'#'*10, y,'#'*20, x.shape, y.shape)
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()