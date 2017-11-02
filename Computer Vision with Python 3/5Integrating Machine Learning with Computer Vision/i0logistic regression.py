from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression


mnist = datasets.load_digits()

images = mnist.images
print(type(images), images.shape)
# print(images[0])

# import matplotlib.pyplot as plt
# plt.gray() 
# plt.matshow(images[0]) 
# plt.show() 

data_size = len(images)

#Preprocessing images
images = images.reshape(len(images), -1)
print(type(images), images.shape)
labels = mnist.target

print('labels=',type(labels), labels.shape, labels[0:20])

#Initialize Logistic Regression
LR_classifier = LogisticRegression(C=0.01, penalty='l1', tol=0.01)

#Training the data on only 75% of the dataset. Rest of the 25% will be used in testing the Logistic Regression
LR_classifier.fit(images[:int((data_size / 4) * 3)], labels[:int((data_size / 4) * 3)])

#Testing the data
predictions = LR_classifier.predict(images[int((data_size / 4)):])
target = labels[int((data_size/4)):]

#Print the performance report of the Logistic Regression model that we learnt
print("Performance Report: \n %s \n" % (metrics.classification_report(target, predictions)))
