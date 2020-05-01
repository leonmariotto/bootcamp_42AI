import numpy as np
from polynomial_model import *
x = np.arange(1,6).reshape(-1, 1)
print(add_polynomial_features(x, 3))
print(add_polynomial_features(x, 6))
