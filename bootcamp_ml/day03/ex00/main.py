import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mylinearregression import MyLinearRegression as MyLR
from tools import *

data = pd.read_csv("spacecraft_data.csv")

Y = np.array(data[['Sell_price']])
Xage = np.array(data[['Age']])

x_train, x_test, y_train, y_test = data_spliter(Xage, Y, 0.7)
myLR_age = MyLR([[1000.0], [-1.0]])
myLR_age.fit_(x_train, y_train)
print("Non-polynomial :", myLR_age.cost_(x_test, y_test))

costs = []
mi = 0

for i in range(2, 12):
    mylr = MyLR([0.0] * i)
    nx_train = add_polynomial_features(x_train, i)
    nx_test = add_polynomial_features(x_test, i)
    mylr.fit_(nx_train, y_train)
    tmp = mylr.cost_(nx_test, y_test)
    if mi < tmp:
        mi = tmp
        ii = i
    costs.append(tmp)

print("Cost =", costs)
print("min =", min(costs))

mylr = MyLR([0.0] * ii)
nx_train = add_polynomial_features(x_train, ii)
nx_test = add_polynomial_features(x_test, ii)
mylr.fit_(nx_train, y_train)
print("The best one, ", ii, "degree, cost :", mylr.cost_(nx_test, y_test))
mylr.plot_polynomial(x_test, y_test, ii)
