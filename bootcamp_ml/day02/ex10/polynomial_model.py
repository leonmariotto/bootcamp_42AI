import numpy as np

def add_polynomial_features(x, power):
    """Add polynomial features to vector
        x by raising its values up to the power given in
        argument.
        Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        power: has to be an int, the power up
        to which the components of vector x are going to
        be raised.
        Returns:
        The matrix of polynomial features as a
        numpy.ndarray, of dimension m * n, containg he
        polynomial feature values for all training examples.
        None if x is an empty numpy.ndarray.
        Raises:
        This function should not raise any Exception.
    """
    nx = np.column_stack((x,)*power)
    for i in range(power):
        nx[:, i] = np.power(nx[:, i], i + 1)
    return nx
