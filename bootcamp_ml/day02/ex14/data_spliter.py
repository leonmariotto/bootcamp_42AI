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

