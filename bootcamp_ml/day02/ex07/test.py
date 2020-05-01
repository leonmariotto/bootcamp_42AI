import numpy as np
from my_linear_regression import MyLinearRegression as MyLR
from sklearn.linear_model import LinearRegression as LR
x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
lr1 = MyLR([2, 0.7])

print("Example 0.0:")
print(lr1.predict_(x))

print("\n\nExample 0.1:")
print(lr1.cost_elem_(lr1.predict_(x),y))

print("\n\nExample 0.2:")
print(lr1.cost_(lr1.predict_(x),y))

print("\n\nExample 1.0:")
lr2 = MyLR([0, 0], 5e-8, 1500000)
#lr2.fit_(x, y)
print(lr2.thetas)

print("\n\nExample 1.1")
print(lr2.predict_(x))
print("\n\nExample 1.2:")
print(lr2.cost_elem_(lr2.predict_(x),y))
print("\n\nExample 1.3:")
print(lr2.cost_(lr2.predict_(x),y))

print("TEST MULTIVARIABLE")
X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
Y = np.array([[23.], [48.], [218.]])
alpha = 0.0001
n_cycle = 160000
mylr = MyLR([[1.], [1.], [1.], [1.], [1]], alpha=alpha, n_cycle=n_cycle)
print("Example 0:")
print(mylr.predict_(X))
print("Expected : array([[8.], [48.], [323.]])")
print("Example 1:")
print(mylr.cost_elem_(X,Y))
print("Expected : array([[37.5], [0.], [1837.5]])")
print("Example 2:")
print(mylr.cost_(X,Y))
print("Expected : 1875.0")
print("Example 3:")
mylr.fit_(X, Y)
print(mylr.thetas)
print("Expected : array([[18.023..], [3.323..], [-0.711..], [1.605..],\
[-0.1113..]])")
print("Example 4:")
print(mylr.predict_(X))
print("Expected : airay([[23.499..], [47.385..], [218.079...]])")
print("Example 5:")
print(mylr.cost_elem_(X,Y))
print("array([[0.041..], [0.062..], [0.001..]])")
print(mylr.cost_(X,Y))
print("Expected : 0.1056")
