import numpy as np
from mylogisticregression import MyLogisticRegression as MyLR
from sklearn.linear_model import LogisticRegression as skLR

X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
Y = np.array([[1], [0], [1]])
Y = np.ravel(Y)
print("Y = ", Y)
mylr = MyLR([2, 0.5, 0, -1.3, 1.09], alpha=1e-6, n_cycle=1000000)
sklr = skLR(tol=1e-6, solver='liblinear', max_iter=1000000)

print(sklr.fit(X, Y))
print(sklr.predict(X))
print(mylr.predict_(X))
print(mylr.cost_(X,Y))

print(mylr.thetas)
print("My fit:\n", mylr.fit_(X, Y))
sklr = sklr.fit(X, Y)
print(sklr.get_params())
print("Sklearn coef:\n", sklr.coef_)
print("Sklearn classes:", sklr.classes_)
print("Sklearn predict_proba:\n", sklr.predict_proba(X))
print("My predict:\n", mylr.predict_(X))
print(mylr.cost_(X,Y))
