import numpy as np
from fit import *

x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta = np.array([[42.], [1.], [1.], [1.]])
print("Example 0:")
theta2 = fit_(x, y, theta, alpha = 0.0005, n_cycle=42000)
print(theta2)
print("Expected : array([[41.99..],[0.97..], [0.77..], [-1.20..]])")
