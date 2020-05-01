import numpy as np

class MyLogisticRegression():
    """
        Description:
        My personnal logistic regression to classify things.
    """
    def __init__(self, theta, alpha=0.001, n_cycle=1000):
        self.alpha = np.array(alpha)
        self.n_cycle = np.array(n_cycle)
        self.thetas = np.array(theta)
        self.thetas = self.thetas.reshape(self.thetas.shape[0], 1)


    def predict_(self, x):
        """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
            Args:
            x: has to be an numpy.ndarray, a vector of dimension m * n.
            theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
            Returns:
            y_hat as a numpy.ndarray, a vector of dimension m * 1.
            None if x or theta are empty numpy.ndarray.
            None if x or theta dimensions are not appropriate.
            Raises:
            This function should not raise any Exception.
        """
        if type(x) is not np.ndarray or x.size == 0:
            return None
        nx = np.array(x)
        nx = np.column_stack((np.ones((nx.shape[0], 1)), nx))
        try:
            predict = np.dot(nx, self.thetas)
            logistic_predict = 1 / (1 + np.exp(-predict))
        except ValueError:
            raise ValueError
        return logistic_predict


    def cost_(self, x, y, eps=1e-15):
        """
            Computes the logistic loss value.
            Args:
            y: has to be an numpy.ndarray, a vector of dimension m * 1.
            y_hat: has to be an numpy.ndarray, a vector of dimension m * 1.
            eps: has to be a float, epsilon (default=1e-15)
            Returns:
            The logistic loss value as a float.
            None on any error.
            Raises:
            This function should not raise any Exception.
        """
        if type(y) is not np.ndarray or y.size == 0:
            return None
        if type(x) is not np.ndarray or x.size == 0:
            return None
        ny_hat = self.predict_(x)
        ny_hat[ny_hat == 0] = eps
        ny_hat[ny_hat == 1] = 1 - eps
        count1 = np.dot(y.T, np.log(ny_hat)).reshape(1,)
        count2 = np.dot((1 - y).T, np.log(1 - ny_hat)).reshape(1,)
        return ((count1 + count2) / y.shape[0])
    
    def fit_(self, x, y):
        """Computes a gradient vector self.n_cycle times from
            two non-empty numpy.ndarray. The two
            arrays must have compatible dimensions.
            Args:
            x: has to be an numpy.ndarray, a matrix of dimension m * n.
            y: has to be an numpy.ndarray, a vector of dimension m * 1.
            theta: has to be an numpy.ndarray, a vector (n +1) * 1.
            Returns:
            The gradient as a numpy.ndarray,
            a vector of dimensions n * 1, containing the result of the
            formula for all j.
            None if x, y, or theta are empty numpy.ndarray.
            None if x, y and theta do not have compatible dimensions.
            Raises:
            This function should not raise any Exception.
        """
        if type(x) is not np.ndarray or x.size == 0:
            return None
        if type(y) is not np.ndarray or y.size == 0:
            return None
        nx = np.array(x)
        nx = np.column_stack((np.ones((nx.shape[0], 1)), nx))
        for i in range(self.n_cycle):
            y_hat = self.predict_(x)
            self.thetas = self.thetas - self.alpha * (np.dot(nx.T, y_hat - y) / y.shape[0])
            self.thetas = self.thetas.reshape(self.thetas.shape[0], 1)
        return self.thetas
