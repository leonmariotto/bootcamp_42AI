import numpy as np
from fit import *
x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
theta= np.array([1, 1])
# Example 0:
theta1 = fit_(x, y, theta, alpha=5e-8, max_iter = 1500000)
print(theta1)

print(predict_(x, theta1))