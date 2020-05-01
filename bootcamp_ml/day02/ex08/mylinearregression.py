import numpy as np
import matplotlib.pyplot as plt

class MyLinearRegression():
    """
        Description:
        My personnal linear regression class to fit like a boss.
    """
    def __init__(self, thetas):
        self.thetas = np.array(thetas).astype(np.float64)

    def fit_(self, x, y, alpha=0.001, n_cycle=1000):
        nx = np.array(x)
        ny = np.array(y)
        try:
            nx.shape[1]
        except IndexError:
            nx = nx.reshape(nx.shape[0], 1)
        try:
            ny.shape[1]
        except IndexError:
            ny = ny.reshape(ny.shape[0], 1)
        try:
            nx = np.column_stack((np.ones((nx.shape[0], 1)), nx))
            for i in range(n_cycle):
                self.thetas = self.thetas.reshape(self.thetas.shape[0], 1)
                y_hat = np.dot(nx, self.thetas)
                #print(self.thetas, i)
                self.thetas -= alpha * (np.dot(nx.T, y_hat - y) / y.shape[0])
            return self.thetas
        except ValueError:
            raise ValueError

    def predict_(self, x):
        nx = np.array(x)
        try:
            nx.shape[1]
        except IndexError:
            nx = nx.reshape(x.shape[0], 1)
        nx = np.column_stack((np.ones((x.shape[0], 1)), x))
        return np.dot(nx, self.thetas)

    def cost_elem_(self, x, y):
        if type(y) is not np.ndarray or y.size == 0:
            return
        if type(x) is not np.ndarray or x.size == 0:
            return
        ny = np.array(y).reshape(y.shape[0], 1)
        ny_hat = self.predict_(x).reshape(y.shape[0], 1)
        q = 1 / (ny.shape[0] * 2)
        return np.power(ny_hat - ny, 2) * q

    def cost_(self, x, y):
        if type(y) is not np.ndarray or y.size == 0:
            return
        if type(x) is not np.ndarray or x.size == 0:
            return
        ny = np.array(y)
        ny_hat = self.predict_(x)
        ny = ny.reshape(ny.shape[0],)
        ny_hat = ny_hat.reshape(ny_hat.shape[0],)
        q = 1 / (ny.shape[0] * 2)
        return np.dot((ny_hat - ny).T, ny_hat - ny) * q

    def mse_(self, x, y):
        if type(y) is not np.ndarray or y.size == 0:
            return
        if type(x) is not np.ndarray or x.size == 0:
            return
        ny = np.array(y)
        ny_hat = self.predict_(x)
        ny = ny.reshape(ny.shape[0],)
        ny_hat = ny_hat.reshape(ny_hat.shape[0],)
        q = 1 / ny.shape[0]
        return np.dot((ny_hat - ny).T, ny_hat - ny) * q

    def plot_hypothesis(self, x, y):
        dataset = np.arange(x.min(), x.max() + 1)
        plt.plot(dataset, self.predict_(dataset))
        plt.plot(x, y, 'g+')
        plt.show()

    def plot_multivariate(self, X, x, y):
        y_hat = self.predict_(X)
        plt.plot(x, y, 'g+')
        plt.plot(x, y_hat, 'r+')
        plt.show()

