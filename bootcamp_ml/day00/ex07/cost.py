import numpy as np

def cost_elem_(y, y_hat):
    """
        Description:
        Calculates all the elements (1/2*M)*(y_pred - y)^2 of the cost function.
        Args:
        y: has to be an numpy.ndarray, a vector.
        y_hat: has to be an numpy.ndarray, a vector.
        Returns:
        J_elem: numpy.ndarray, a vector
        of dimension (number of the training examples,1).
        None if there is a dimension matching problem between X, Y or theta.
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
        y_hat = y_hat.reshape((y.shape[0], 1))
    if y.shape != y_hat.shape:
        return None
    l = 1 / (y.shape[0] * 2)
    return np.power((y_hat - y), 2) * l


def cost_(y, y_hat):
    """
        Description:
        Calculates the value of cost function.
        Args:
        y: has to be an numpy.ndarray, a vector.
        y_hat: has to be an numpy.ndarray, a vector.
        Returns:
        J_value : has to be a float.
        None if there is a dimension matching problem between X, Y or theta.
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
        y_hat = y_hat.reshape((y.shape[0], 1))
    if y.shape != y_hat.shape:
        return None
    return cost_elem_(y, y_hat).sum()

