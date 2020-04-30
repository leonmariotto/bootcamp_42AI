import numpy as np
from scipy.stats import zscore as spzs
from myzscore import *
X = np.array([0, 15, -9, 7, 12, 3, -21])
print(zscore(X))
print(spzs(X))
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(zscore(Y))
print(spzs(Y))
