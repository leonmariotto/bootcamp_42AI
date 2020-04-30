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
lr2.fit_(x, y)
print(lr2.thetas)

print("\n\nExample 1.1")
print(lr2.predict_(x))
print("\n\nExample 1.2:")
print(lr2.cost_elem_(lr2.predict_(x),y))
print("\n\nExample 1.3:")
print(lr2.cost_(lr2.predict_(x),y))

