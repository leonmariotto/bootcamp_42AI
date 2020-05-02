import numpy as np
from sklearn.metrics import confusion_matrix
from confusion_matrix import confusion_matrix_
y_hat = np.array(['norminet', 'dog', 'norminet', 'norminet', 'dog', 'bird'])
y = np.array(['dog', 'dog', 'norminet', 'norminet', 'dog', 'norminet'])
print("Mine:", confusion_matrix_(y, y_hat))
print("Sklearn:", confusion_matrix(y, y_hat))
print("Mine:", confusion_matrix_(y, y_hat, labels=['dog', 'norminet']))
print("Sklearn:", confusion_matrix(y, y_hat, labels=['dog', 'norminet']))
