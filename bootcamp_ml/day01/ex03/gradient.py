import numpy as np

def add_intercept(x):
    """Adds a column of 1's to the non-empty numpy.ndarray x.
        Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        Returns:
        X as a numpy.ndarray, a vector of dimension m * 2.
        None if x is not a numpy.ndarray.
        None if x is a empty numpy.ndarray.
        Raises:
        This function should not raise any Exception.
    """
    if type(x) is not np.ndarray or x.size == 0:
        print("Arg have t0 be a non-empty np.ndarray")
        return None
    return np.column_stack((np.ones((x.shape[0], 1)), x))


def predict_(x, theta):
    """Computes the prediction vector y_hat from two non-empty numpy.ndarray.
        Args:
        x: has to be an numpy.ndarray, a vector of dimensions m * 1.
        theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
        Returns:
        y_hat as a numpy.ndarray, a vector of dimension m * 1.
        None if x or theta are empty numpy.ndarray.
        None if x or theta dimensions are not appropriate.
        Raises:
        This function should not raise any Exception.
    """

    if type(x) is not np.ndarray:
        print("Only numpy.ndarray")
        return None
    if theta.size == 0 or x.size == 0:
        print("Only numpy.ndarray not empty")
        return None
    try:
        x.shape[1]
        theta.shape[1]
    except IndexError:
        x = x.reshape(x.shape[0], 1)
        theta = theta.reshape(theta.shape[0], 1)

    x = add_intercept(x)
    if x.any() == None:
        return None
    try:
        return np.dot(x, theta).astype(np.float32)
    except ValueError:
        return None 


def simple_gradient(x, y, theta):
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
    y_hat = predict_(x, theta)
    try:
        return np.array([(y_hat - y).sum(), np.dot((y_hat - y).T, x)[0][0]]) / y.shape[0]
    except ValueError:
        return None
