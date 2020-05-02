import numpy as np
import pandas as pd
from tools import *
from sklearn.linear_model import LogisticRegression as skLR

datasetX = pd.read_csv('../resources/solar_system_census.csv')
datasetY = pd.read_csv('../resources/solar_system_census_planets.csv')

X = np.array(datasetX[['height', 'weight', 'bone_density']])
Y = np.array(datasetY[['Origin']])

x_train, x_test, y_train, y_test = data_spliter(X, Y, 0.7)

y_test = np.ravel(y_test)
ny_train = np.ravel(np.array(y_train))
ny_train[ny_train != 3] = 0

sklr = skLR(tol=1e-6, solver='liblinear', max_iter=1000000)

Unisklr = sklr.fit(x_train, ny_train)
print("Uni Sklearn predict \n:", Unisklr.predict(x_test))
print("Uni Sklearn predict_proba:\n", sklr.predict_proba(x_test))
Multisklr = sklr.fit(x_train, y_train)
print("Multi Sklearn predict \n:", Multisklr.predict(x_test))
print("Multi Sklearn predict_proba:\n", sklr.predict_proba(x_test))
