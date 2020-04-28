import numpy as np

def cost_(y, y_hat):
    """Computes the mean squared error of two non-empty 
        numpy.ndarray, without any for loop.
        The two arrays must have the same dimensions.
        Args:
        y: has to be an numpy.ndarray, a vector.
        y_hat: has to be an numpy.ndarray, a vector.
        Returns:
        The mean squared error of the two vectors as a float.
        None if y or y_hat are empty numpy.ndarray.
        None if y and y_hat does not share the same dimensions.
        Raises:
        This function should not raise any Exception.
    """
    if type(y) is not np.ndarray or type(y_hat) is not np.ndarray:
        return None
    if y.all() is None or y_hat.all() is None:
        return None
    try:
        y.shape[1]
        y_hat.shape[1]
    except IndexError:
        y = y.reshape((y.shape[0], 1))
        y_hat = y_hat.reshape((y_hat.shape[0], 1))
    if y.shape != y_hat.shape:
        return None
    q = 1 / (y.shape[0] * 2)
    return np.dot((y_hat - y).T, y_hat - y) * q
