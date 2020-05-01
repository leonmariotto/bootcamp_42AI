import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mylinearregression import MyLinearRegression as MyLR
from add_poly import *

data = pd.read_csv("spacecraft_data.csv")

Y = np.array(data[['Sell_price']])
Xage = np.array(data[['Age']])

myLR_age = MyLR([[1000.0], [-1.0]])
myLR_age.fit_(Xage, Y)
print("Non-polynomial :", myLR_age.cost_(Xage, Y))

costs = []

for i in range(2, 12):
    mylr = MyLR([0.0] * i)
    nXage = add_polynomial_features(Xage, i)
    mylr.fit_(nXage, Y)
    costs.append(mylr.cost_(nXage, Y))
    mylr.plot_polynomial(Xage, Y, i)

print("Cost =", costs)
print("min =", min(costs))

mylr = MyLR([0.0] * 10)
nXage = add_polynomial_features(Xage, 10)
mylr.fit_(nXage, Y)
print("The best one, 10 degree, cost :", mylr.cost_(nXage, Y))
mylr.plot_polynomial(Xage, Y, 10)
