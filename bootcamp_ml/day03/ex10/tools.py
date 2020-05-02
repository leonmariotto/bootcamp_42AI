import numpy as np


def data_spliter(x, y, proportion):
    """Shuffles and splits the dataset
        (given by x and y) into a training and a test set,
        while respecting the given proportion
        of examples to be kept in the traning set.
        Args:
        x: has to be an numpy.ndarray, a matrix of dimension m * n.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        proportion: has to be a float,
        the proportion of the dataset that will be assigned to
        the training set.
        Returns:
        (x_train, x_test, y_train, y_test) as a tuple of numpy.ndarray
        None if x or y is an empty numpy.ndarray.
        None if x and y do not share compatible dimensions.
        Raises:
        This function should not raise any Exception.
    """ 
    if type(x) is not np.ndarray or x.size == 0:
        return None
    if type(y) is not np.ndarray or y.size == 0:
        return None
    if x.shape[0] != y.shape[0]:
        return None
    m = x.shape[0]
    try:
        n = x.shape[1]
    except IndexError:
        n = 1
    nx = np.column_stack((x, y))
    np.random.shuffle(nx)
    q = int(m * proportion)
    return (nx[:q, :n], nx[q:, :n], nx[:q, n:], nx[q:, n:])


def zscore(x):
    """Computes the normalized version
        of a non-empty numpy.ndarray using the z-score
        standardization.
        Args:
        x: has to be an numpy.ndarray, a vector.
        Returns:
        x' as a numpy.ndarray.
        None if x is a non-empty numpy.ndarray.
        Raises:
        This function shouldn't raise any Exception.
    """
    if type(x) is not np.ndarray or x.size == 0:
        return None
    u = x.mean()
    o = np.std(x)

    return (x - u) / o


def add_polynomial_features(x, power):
    """
        Add polynomial features to vector
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
