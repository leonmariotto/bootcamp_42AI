import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
from other_costs import *

x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])
print("Mean squared error")
print("your implementation")
print(mse_(x,y))
print("sklearn implementation")
print(mean_squared_error(x,y))
print("Root mean squared error")
print("your implementation")
print(rmse_(x,y))
print("sklearn implementation")
print(sqrt(mean_squared_error(x,y)))
print("Mean absolute error")
print("your implementation")
print(mae_(x,y))
print("sklearn implementation")
print(mean_absolute_error(x,y))
print("R2-score")
print("your implementation")
print(r2score_(x,y))
print("sklearn implementation")
print(r2_score(x,y))
