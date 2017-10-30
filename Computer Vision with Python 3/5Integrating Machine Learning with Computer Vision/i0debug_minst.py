from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression


mnist = datasets.load_digits()

images = mnist.images
# print(type(images), images.shape)
# print(images[0][0], images[1][0],images[2][1])

import matplotlib.pyplot as plt
plt.gray()
for i in range(3):
# plt.matshow(images[0])
    plt.figure()
    plt.imshow(images[i])
plt.show() 