import numpy as np

def log_loss_(y, y_hat, eps=1e-15):
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
    if type(y_hat) is not np.ndarray or y_hat.size == 0:
        return None
    ny_hat = np.array(y_hat)
    ny_hat[y_hat == 0] = eps
    ny_hat[y_hat == 1] = 1 - eps
    count1 = np.dot(y.T, np.log(ny_hat)).reshape(1,)
    count2 = np.dot((1 - y).T, np.log(1 - y_hat)).reshape(1,)
    return ((count1 + count2) / y.shape[0])
