from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split


mnist = fetch_mldata('MNIST original')

images = mnist.data
labels = mnist.target

# print('len(images)=', len(images))


# print(images[0],'\n')
images = normalize(images, norm='l2')
# print(images[0])

images_train, images_test, labels_train, labels_test =\
    train_test_split(images, labels, test_size=0.25, random_state=17)

nn = MLPClassifier(hidden_layer_sizes=(200), max_iter=20, solver='sgd',
                    learning_rate_init=0.001, verbose=True)

nn.fit(images_train, labels_train)
print('Network Performance: %f' % nn.score(images_test, labels_test))