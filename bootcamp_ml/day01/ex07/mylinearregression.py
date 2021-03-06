import numpy as np
import matplotlib.pyplot as plt


class MyLinearRegression():
    """
        Description:
        My personnal linear regression class to fit like a boss.
    """
    def __init__(self, thetas, alpha=0.001, n_cycle=1000):
        self.alpha = alpha
        self.n_cycle = n_cycle
        self.thetas = np.array(thetas).reshape(2,)

    def fit_(self, x, y):
        nx = np.array(x)
        ny = np.array(y)
        if (
                type(ny) is not np.ndarray or ny.size == 0 or
                type(nx) is not np.ndarray or nx.size == 0
           ):
            return
        try:
            nx.shape[1]
            ny.shape[1]
        except IndexError:
            nx = nx.reshape(nx.shape[0], 1)
            ny = ny.reshape(ny.shape[0], 1)
        try:
            nx = np.column_stack((np.ones((nx.shape[0], 1)), nx))
            for i in range(self.n_cycle):
                ny_hat = np.dot(nx, self.thetas).astype(np.float32)\
                .reshape(ny.shape[0], 1)
                self.thetas = self.thetas - self.alpha *\
                (np.dot((ny_hat - ny).T, nx[:]) / ny.shape[0])
                self.thetas = self.thetas.reshape(2,)
        except ValueError:
            return

    def predict_(self, x):
        nx = np.array(x)
        if (
                type(nx) is not np.ndarray or nx.size == 0
           ):
            return
        try:
            nx.shape[1]
        except IndexError:
            nx = nx.reshape(x.shape[0], 1)
        nx = np.column_stack((np.ones((x.shape[0], 1)), x))
        return np.dot(nx, self.thetas.reshape(2,1)).astype(np.float32)

    def cost_elem_(self, y_hat, y):
        ny = np.array(y)
        ny_hat = np.array(y_hat)
        if (
                type(ny) is not np.ndarray or ny.size == 0 or
                type(ny_hat) is not np.ndarray or ny_hat.size == 0
           ):
            return
        ny_hat = ny_hat.reshape(ny_hat.shape[0], 1)
        ny = ny.reshape(ny.shape[0], 1)
        q = 1 / (ny.shape[0] * 2)
        return np.power(ny_hat - ny, 2) * q

    def cost_(self, y_hat, y):
        ny = np.array(y)
        ny_hat = np.array(y_hat)
        if type(ny) is not np.ndarray or ny.size == 0:
            return
        if type(ny_hat) is not np.ndarray or ny_hat.size == 0:
            return
        ny = ny.reshape(ny.shape[0],)
        ny_hat = ny_hat.reshape(ny_hat.shape[0],)
        q = 1 / (ny.shape[0] * 2)
        return np.dot((ny_hat - ny).T, ny_hat - ny) * q

    def mse_(self, x, y):
        ny = np.array(y)
        ny_hat = self.predict_(x)
        if type(ny) is not np.ndarray or ny.size == 0:
            return
        if type(ny_hat) is not np.ndarray or ny_hat.size == 0:
            return
        ny = ny.reshape(ny.shape[0],)
        ny_hat = ny_hat.reshape(ny_hat.shape[0],)
        q = 1 / (ny.shape[0])
        return np.dot((ny_hat - ny).T, ny_hat - ny) * q

    def plot_hypothesis(self, x, y):
        self.fit_(x, y)
        dataset = np.arange(x.min(), x.max() + 1)
        plt.plot(dataset, self.predict_(dataset))
        plt.plot(x, y, 'r+')
        plt.show()
