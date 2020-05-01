import numpy as np
X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

print("Example 1:")
print(cost_(X, Y))
print("Expected : 4.285714285714286")
print("Example 2:")
print(cost_(X, X))
print("Expected : 0.0")
