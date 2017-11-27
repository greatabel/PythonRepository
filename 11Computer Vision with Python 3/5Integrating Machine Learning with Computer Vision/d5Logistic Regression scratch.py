# https://www.codelast.com/%E5%8E%9F%E5%88%9B-%E7%94%A8%E4%BA%BA%E8%AF%9D%E8%A7
# %A3%E9%87%8A%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E4%B8%AD%E7%9A%84logistic-regression
# %EF%BC%88%E9%80%BB%E8%BE%91%E5%9B%9E%E5%BD%92%EF%BC%89/

# https://beckernick.github.io/logistic-regression-from-scratch/
# https://datascienceplus.com/building-a-logistic-regression-in-python-step-by-step/
import numpy as np
import matplotlib.pyplot as plt
# Generating Data

np.random.seed(0)
num_observations = 5000

x1 = np.random.multivariate_normal([0, 0], [[1, .75],[.75, 1]], num_observations)
x2 = np.random.multivariate_normal([1, 4], [[1, .75],[.75, 1]], num_observations)

simulated_separableish_features = np.vstack((x1, x2)).astype(np.float32)

simulated_labels = np.hstack((np.zeros(num_observations),
                              np.ones(num_observations)))

# print('x1.shape, x2.shape >', x1.shape, x2.shape)
# print('simulated_separableish_features.shape>', simulated_separableish_features.shape)
# print('simulated_labels.shape>', simulated_labels.shape)
# print('x1, x2 >', x1, x2)
# print('simulated_separableish_features>', simulated_separableish_features)
# print('simulated_labels>', simulated_labels)
# print('simulated_separableish_features[:, 0]>', simulated_separableish_features[:, 0])
# print('simulated_separableish_features[:, 1]>', simulated_separableish_features[:, 1])


# plt.figure(figsize=(12,8))
# plt.scatter(simulated_separableish_features[:, 0], simulated_separableish_features[:, 1],
#             c = simulated_labels, alpha = .4)
# plt.show()

def sigmoid(scores):
    return 1 / (1 + np.exp(-scores))

def log_likelihood(features, target, weights):
    scores = np.dot(features, weights)
    ll = np.sum( target*scores - np.log(1 + np.exp(scores)) )
    return ll

def logistic_regression(features, target, num_steps, learning_rate, add_intercept = False):
    if add_intercept:
        intercept = np.ones((features.shape[0], 1))
        features = np.hstack((intercept, features))
        
    weights = np.zeros(features.shape[1])
    
    for step in range(num_steps):
        scores = np.dot(features, weights)
        predictions = sigmoid(scores)

        # Update weights with gradient
        output_error_signal = target - predictions
        gradient = np.dot(features.T, output_error_signal)
        weights += learning_rate * gradient
        
        # Print log-likelihood every so often
        if step % 10000 == 0:
            print(log_likelihood(features, target, weights))
        
    return weights

weights = logistic_regression(simulated_separableish_features, simulated_labels,
                     num_steps = 300000, learning_rate = 5e-5, add_intercept=True)

data_with_intercept = np.hstack((np.ones((simulated_separableish_features.shape[0], 1)),
                                 simulated_separableish_features))
final_scores = np.dot(data_with_intercept, weights)
preds = np.round(sigmoid(final_scores))

print('Accuracy from scratch: {0}'.format((preds == simulated_labels).sum().astype(float) / len(preds))  )
# print('Accuracy from sk-learn: {0}'.format(clf.score(simulated_separableish_features, simulated_labels)) )

plt.figure(figsize = (12, 8))
plt.scatter(simulated_separableish_features[:, 0], simulated_separableish_features[:, 1],
            c = preds == simulated_labels - 1, alpha = .8, s = 50)
plt.show()