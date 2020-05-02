import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from other_metrics import *

y_hat = np.array([1, 1, 0, 1, 0, 0, 1, 1])
y = np.array([1, 0, 0, 1, 0, 1, 0, 0])

print("Mine:", accuracy_score_(y, y_hat))
print("Sklearn:", accuracy_score(y, y_hat))

print("Mine:", precision_score_(y, y_hat))
print("Sklearn:", precision_score(y, y_hat))

print("Mine:", recall_score_(y, y_hat))
print("Sklearn:", recall_score(y, y_hat))

print("Mine:", f1_score_(y, y_hat))
print("Sklearn:", f1_score(y, y_hat))

y_hat = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'dog', 'dog', 'dog'])
y = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet', 'dog', 'norminet'])

print("Mine:", accuracy_score_(y, y_hat))
print("Sklearn:", accuracy_score(y, y_hat))

print("Mine:", precision_score_(y, y_hat, pos_label='dog'))
print("Sklearn:", precision_score(y, y_hat, pos_label='dog'))

print("Mine:", recall_score_(y, y_hat, pos_label='dog'))
print("Sklearn:", recall_score(y, y_hat, pos_label='dog')) 

print("Mine:", f1_score_(y, y_hat, pos_label='dog'))
print("Sklearn:", f1_score(y, y_hat, pos_label='dog'))

y_hat = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'dog', 'dog', 'dog'])
y = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet', 'dog', 'norminet'])

print("Mine:", accuracy_score_(y, y_hat))
print("Sklearn:", accuracy_score(y, y_hat))

print("Mine:", precision_score_(y, y_hat, pos_label='norminet'))
print("Sklearn:", precision_score(y, y_hat, pos_label='norminet'))

print("Mine:", recall_score_(y, y_hat, pos_label='norminet'))
print("Sklearn:", recall_score(y, y_hat, pos_label='norminet'))

print("Mine:", f1_score_(y, y_hat, pos_label='norminet'))
print("Sklearn:", f1_score(y, y_hat, pos_label='norminet'))
