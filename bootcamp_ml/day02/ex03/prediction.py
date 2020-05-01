import numpy as np

def predict_(x, theta):
    """
        Computes the prediction vector y_hat from two non-empty numpy.ndarray.
        Args:
        x: has to be an numpy.ndarray, a matrix of dimension m * n.
        theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
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
    if type(theta) is not np.ndarray:
        print("Only numpy.ndarray")
        return None
    if theta.size == 0 or x.size == 0:
        print("Only numpy.ndarray not empty")
        return None
    x = np.column_stack((np.ones((x.shape[0], 1)), x))
    return np.dot(x, theta).astype(np.float32)
