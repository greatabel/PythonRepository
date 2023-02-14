'''
绘制qq图，平均超额图和hill图，
再用极大似然法进行广义帕累托拟合和KS法检验）提供代码和对数据结果的解析

'''

import csv


import seaborn as sns

import lifelines
import scipy
import numpy as np

import statsmodels.api as sm
import matplotlib.pyplot as plt


# Open the CSV file
with open('hill_sample.csv', 'r') as f:
    # Read the CSV file using the csv.reader function
    reader = csv.reader(f)
    # Use a list comprehension to extract the data from the first (and only) column
    data0 = [float(row[0]) for row in reader]

# Convert the list to a numpy array
data = np.array(data0)
print(data[0:10])

# 测试小批量数据, 使用全量数据时候注释掉下面一行
data = data[0:2000]
print(len(data))


# # 华为qq图
# fig = sm.qqplot(data, line='45')
# plt.show()

# qq图
sns.distplot(data, fit=scipy.stats.expon, kde=False)
plt.show()

# 绘制平均超额图
sns.regplot(x=np.sort(data), y=np.arange(1, len(data)+1)/len(data))
plt.show()


# 绘制hill图：
sns.regplot(x=np.sort(data), y=np.arange(1, len(data)+1)/len(data), scatter=False)
plt.show()

'''
数据解析
在qq图中，红色的参考线代表理论分布（此处使用指数分布），
如果数据分布与参考线近似，则数据可近似为该分布。从图中可以看出，该数据不太适合我们选择的规律分布。


平均超额图显示了超过阈值的事件数与阈值之间的关系。从图中可以看出，数据在阈值以上增长较缓慢。


Hill图显示了对数概率与对数阈值之间的关系，可以看出数据的尾部行为。

帕累托拟合图显示了数据的累积分布函数，可以看出数据的尾部分布是否符合幂律分布。
在拟合GPD之后，程序将数据与拟合的GPD进行比较，
可以看出模型在某些区域拟合效果较好，但在一些他区域效果不佳。

最后使用KS检验来评估模型拟合的好坏，
得到了KS统计量和P值，可以看出模型在该数据集上的拟合效果不一般
'''


# Define the negative log-likelihood function for the GPD
def neg_log_likelihood_gpd(params, data):
    shape, scale = params
    if shape <= 0 or scale <= 0:
        return np.inf
    return -np.sum(np.log(shape / scale * (1 + shape * np.array(data) / scale)**(-1 - 1 / shape)))

# # Example data
# data = [86.91801635, 24.01706689, 23.3389752, 21.34924596, 20.89329284, 20.87855024,
#         20.65259539, 20.41830382, 19.7074104, 18.91462623, 18.44100016]
'''

使用了 L-BFGS-B 算法来最小化函数，该算法需要指定一个初始参数 x0，
这只是一个开始点，最后的结果可能会依赖于x0的选择\
'''
# Fit the GPD to the data using maximum likelihood
fit_params = scipy.optimize.minimize(neg_log_likelihood_gpd, x0=[1, 1], args=(data,), method='L-BFGS-B')

# Plot the data and the fitted GPD
x = np.linspace(0, 100, 1000)
pdf = fit_params.x[0] / fit_params.x[1] * (1 + fit_params.x[0] * x / fit_params.x[1])**(-1 - 1 / fit_params.x[0])
plt.plot(x, pdf, label='Fitted GPD')
plt.hist(data, bins=20, density=True, alpha=0.5, label='Data')
plt.legend()
plt.show()

print('-*'*20, 'KS test', '-*'*20)
# Perform the KS test
D, p_value = scipy.stats.ks_2samp(data, pdf)
print('KS test statistic: ', D)
print('p-value: ', p_value)

plt.show()





