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

print("Cost =", costs)
print("min =", min(costs))

plt.bar(np.arange(2,12), costs, 1)
plt.show()
