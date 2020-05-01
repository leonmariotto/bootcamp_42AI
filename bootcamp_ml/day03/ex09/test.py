import numpy as np
from mylogisticregression import MyLogisticRegression as MyLR

X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
Y = np.array([[1], [0], [1]])
mylr = MyLR([2, 0.5, 0, -1.3, 1.09], alpha=1e-6, n_cycle=1000000)

print(mylr.predict_(X))
print(mylr.cost_(X,Y))

print(mylr.thetas)
print(mylr.fit_(X, Y))

print(mylr.predict_(X))
print(mylr.cost_(X,Y))

