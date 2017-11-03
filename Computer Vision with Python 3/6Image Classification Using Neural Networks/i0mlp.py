from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split


mnist = fetch_mldata('MNIST original')

images = mnist.data
labels = mnist.target

print('len(images)=', len(images))

# print(images[0],'\n')
images = normalize(images, norm='l2')
# print(images[0])
