import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR

data = pd.read_csv("spacecraft_data.csv")

print("PART ONE : UNIVARIATE LINEAR REGRESSION")

Xage = np.array(data[['Age']])
Xthrust = np.array(data[['Thrust_power']])
Xtera = np.array(data[['Terameters']])
Y = np.array(data[['Sell_price']])

myLR_age = MyLR([[1000.0], [-1.0]])
myLR_age.fit_(Xage[:,0].reshape(-1,1), Y, alpha = 2.5e-5, n_cycle = 100000)
myLR_age.plot_hypothesis(Xage, Y)

myLR_thrust = MyLR([[0], [10.0]])
myLR_thrust.fit_(Xthrust[:,0].reshape(-1,1), Y, alpha = 1.0e-5, n_cycle = 100000)
myLR_thrust.plot_hypothesis(Xthrust, Y)

myLR_tera = MyLR([[800.0], [-1.0]])
myLR_tera.fit_(Xtera[:,0].reshape(-1,1), Y, alpha = 2.5e-5, n_cycle = 100000)
myLR_tera.plot_hypothesis(Xtera, Y)


print("PART TWO : MULTIVARIATE LINEAR REGRESSION ( A NEW HOPE )")

X = np.array(data[['Age','Thrust_power','Terameters']])
my_lreg = MyLR([300.0, 1.0, 1.0, 1.0])

print(my_lreg.mse_(X, Y))
my_lreg.fit_(X, Y, alpha=1e-5, n_cycle=600000)
print(my_lreg.thetas)
print(my_lreg.mse_(X, Y))
my_lreg.plot_multivariate(X, Xage, Y)
my_lreg.plot_multivariate(X, Xthrust, Y)
my_lreg.plot_multivariate(X, Xtera, Y)
