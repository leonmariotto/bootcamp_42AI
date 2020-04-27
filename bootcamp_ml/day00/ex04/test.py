import numpy as np
from tools import add_intercept

# Example 1:
x = np.arange(1, 6)
print(add_intercept(x))
# Example 2:
y = np.arange(1, 10).reshape((3, 3))
print(add_intercept(y))
