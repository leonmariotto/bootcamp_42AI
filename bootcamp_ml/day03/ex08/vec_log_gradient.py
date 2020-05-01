import numpy as np
from log_pred import logistic_predict

def vec_log_gradient(x, y, theta):
    """Computes a gradient vector from
        three non-empty numpy.ndarray, with a for-loop. The three
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
    if type(theta) is not np.ndarray or theta.size == 0:
        return None
    y_hat = logistic_predict(x, theta)
    nx = np.array(x)
    nx = np.column_stack((np.ones((nx.shape[0], 1)), nx))
    return np.dot(nx.T, y_hat - y) / y.shape[0]
