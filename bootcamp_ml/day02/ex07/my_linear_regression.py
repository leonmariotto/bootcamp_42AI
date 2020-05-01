import numpy as np

class MyLinearRegression():
    """
        Description:
        My personnal linear regression class to fit like a boss.
    """
    def __init__(self, thetas, alpha=0.001, n_cycle=1000):
        self.alpha = alpha
        self.n_cycle = n_cycle
        self.thetas = np.array(thetas).astype(np.float64)

    def fit_(self, x, y):
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
            for i in range(self.n_cycle):
                self.thetas = self.thetas.reshape(self.thetas.shape[0], 1)
                y_hat = np.dot(nx, self.thetas)
#                print(self.alpha * (np.dot(nx.T, y_hat - y) / y.shape[0]))
                self.thetas -= self.alpha * (np.dot(nx.T, y_hat - y) / y.shape[0])
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
