import numpy as np
from cost import cost_
X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
# Example 1:
print(cost_(X, Y))
# Example 2:
print(cost_(X, X))