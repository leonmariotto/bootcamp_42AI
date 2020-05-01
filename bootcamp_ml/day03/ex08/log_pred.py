import numpy as np

def logistic_predict(x, theta):
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
    if type(theta) is not np.ndarray or theta.size == 0:
        return None
    nx = np.array(x)
    nx = np.column_stack((np.ones((nx.shape[0], 1)), nx))
    try:
        predict = np.dot(nx, theta)
        logistic_predict = 1 / (1 + np.exp(-predict))
    except ValueError:
        raise ValueError
    return logistic_predict
