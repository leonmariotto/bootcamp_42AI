import numpy as np

def gradient(x, y, theta):
    """Computes a gradient vector from three non-empty
        numpy.ndarray, without any for-loop.
        The three arrays must have compatible dimensions.
        Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a 2 * 1 vector.
        Returns:
        The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
        None if x, y, or theta are empty numpy.ndarray.
        None if x, y and theta do not have compatible dimensions.
        Raises:
        This function should not raise any Exception.
    """
    try:
        x.shape[1]
        y.shape[1]
    except IndexError:
        x = x.reshape(x.shape[0], 1)
        y = y.reshape(y.shape[0], 1)
    if type(y) is not np.ndarray or y.size == 0:
        return None
    if type(x) is not np.ndarray or x.size == 0:
        return None
    if type(theta) is not np.ndarray or theta.size == 0:
        return None
    try:
        x = np.column_stack((np.ones((x.shape[0], 1)), x))
        y_hat = np.dot(x, theta).astype(np.float32).reshape(y.shape[0], 1)
        return theta - np.dot((y_hat - y).T, x[:]) / y.shape[0]
    except ValueError:
        return None
