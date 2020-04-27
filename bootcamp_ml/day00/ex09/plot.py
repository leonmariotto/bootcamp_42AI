import numpy as np
import matplotlib.pyplot as plt


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
    return np.column_stack((np.ones_like(x), x))


def cost_elem_(y, y_hat):
    """
        Description:
        Calculates all the elements
            (1/2*M)*(y_pred - y)^2 of the cost function.
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
    q = 1 / (len(y) * 2)
    return np.power((y_hat - y), 2) * q


def cost_(y, y_hat):
    """Computes the mean squared error of two non-empty
            numpy.ndarray, without any for loop.
        , →
        The two arrays must have the same dimensions.
        Args:
        y: has to be an numpy.ndarray, a vector.
        y_hat: has to be an numpy.ndarray, a vector.
        Returns:
        The mean squared error of the two vectors as a float.
        None if y or y_hat are empty numpy.ndarray.
        None if y and y_hat does not share the same dimensions.
        Raises:
        This function should not raise any Exceptions.
    """
    if type(y) is not np.ndarray or type(y_hat) is not np.ndarray:
        return None
    if y.all() is None or y_hat.all() is None:
        return None
    if y.shape != y_hat.shape:
        return None
    q = 1 / (y.shape[0] * 2)
    return np.dot((y_hat - y).T, y_hat - y) * q


def predict_(x, theta):
    """Computes the vector of prediction
        y_hat from two non-empty numpy.ndarray.
        Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
        Returns:
        y_hat as a numpy.ndarray, a vector of dimension m * 1.
        None if x or theta are empty numpy.ndarray.
        None if x or theta dimensions are not appropriate.
        Raises:
        This function should not raise any Exceptions.
    """

    if theta.size == 0:
        print("Only numpy.ndarray not empty")
    if theta.shape != (2,):
        print("Theta have to be a numpy.ndarray (2 x 1)")
        return None

    x = add_intercept(x)
    if x.any() is None:
        return None
    return np.dot(x, theta).astype(np.float32)


def plot_with_cost(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
        Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
        Returns:
        Nothing.
        Raises:
        This function should not raise any Exception.
    """
    if type(x) is not np.ndarray or x.size == 0:
        return
    if type(y) is not np.ndarray or y.size == 0:
        return
    if type(theta) is not np.ndarray or theta.size == 0:
        return
    dataset = np.arange(x.min(), x.max() + 1)
    plt.plot(dataset, predict_(dataset, theta))
    for i in range(len(x)):
        plt.plot([x[i]]*2, [y[i], theta[0] + theta[1]
                 * x[i]], c='r', ls='dotted')
    plt.plot(x, y, 'b+')
    plt.show()
