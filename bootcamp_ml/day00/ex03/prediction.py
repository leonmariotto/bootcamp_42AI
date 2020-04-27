import numpy as np


def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from
        two non-empty numpy.ndarray.
        Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
        Returns:
        y_hat as a numpy.ndarray, a vector of dimension m * 1.
        None if x or theta are empty numpy.ndarray.
        None if x or theta dimensions are not appropriate.
        Raises:
        This function should not raise any Exception.
    """

    if type(x) is not np.ndarray or type(theta) is not np.ndarray:
        print("Type error, only numpy.ndarray")
        return None
    if x.size == 0 or theta.size == 0:
        print("Only numpy.ndarray not empty")
    if len(x.shape) != 1 and x.shape[1] != 1:
        print("First arg have to be a Vector")
        return None
    if theta.shape != (2,):
        print("Theta have to be a numpy.ndarray (2 x 1)")
        return None

    x = np.column_stack((np.ones_like(x), x))
    return np.dot(x, theta).astype(np.float32)
