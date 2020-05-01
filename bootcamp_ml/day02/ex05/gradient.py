import numpy as np

def gradient(x, y, theta):
    """Computes a gradient vector from
        three non-empty numpy.ndarray, without any for-loop.
        The three arrays must have the compatible dimensions.
        Args:
        x: has to be an numpy.ndarray, a matrix of dimension m * n.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector (n +1) * 1.
        Returns:
        The gradient as a numpy.ndarray,
        a vector of dimensions n * 1, containg the result of
        the formula for all j.
        None if x, y, or theta are empty numpy.ndarray.
        None if x, y and theta do not have compatible dimensions.
        Raises:
        This function should not raise any Exception.
    """
    if (
            type(y) is not np.ndarray or y.size == 0 or
            type(x) is not np.ndarray or x.size == 0 or
            type(theta) is not np.ndarray or theta.size == 0
       ):
        return None
    try:
        x.shape[1]
    except IndexError:
        x = x.reshape(x.shape[0], 1)
    try:
        y.shape[1]
    except IndexError:
        y = y.reshape(y.shape[0], 1)
    try:
        x = np.column_stack((np.ones((x.shape[0], 1)), x))
        theta = theta.reshape(theta.shape[0], 1)
        y_hat = np.dot(x, theta)
        theta = (np.dot(x.T, y_hat - y) / y.shape[0])
        return theta
    except ValueError:
        raise ValueError

