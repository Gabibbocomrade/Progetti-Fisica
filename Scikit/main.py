from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
# split it in features and labels
X = iris.data()
y = iris.target()

print(X.shape)
print(y.shape)