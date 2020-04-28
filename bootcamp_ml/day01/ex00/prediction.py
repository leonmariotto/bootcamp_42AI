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

    if theta.size == 0:
        print("Only numpy.ndarray not empty")
    if theta.shape != (2,) and theta.shape != (2, 1):
        print("Theta have to be a numpy.ndarray (2 x 1)")
        return None

    x = add_intercept(x)
    if x.any() == None:
        return None
    return np.dot(x, theta).astype(np.float32)
