from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
# split it in features and labels
X = iris.data
y = iris.target

print(X.shape)
print(y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)