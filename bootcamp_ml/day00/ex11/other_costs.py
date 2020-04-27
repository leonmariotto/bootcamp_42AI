import numpy as np



def mse_(y, y_hat):
    """
        Description:
        Calculate the MSE between the predicted output and the real output.
        Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
        Returns:
        mse: has to be a float.
        None if there is a matching dimension problem.
        Raises:
        This function should not raise any Exceptions.
    """
    if type(y) is not np.ndarray or type(y_hat) is not np.ndarray:
        return None
    if y.all() is None or y_hat.all() is None:
        return None
    if y.shape != y_hat.shape:
        return None
    q = 1 / y.shape[0]
    return float(np.dot((y_hat - y).T, y_hat - y) * q)


def rmse_(y, y_hat):
    """
        Description:
        Calculate the RMSE between the predicted output and the real output.
        Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
        Returns:
        rmse: has to be a float.
        None if there is a matching dimension problem.
        Raises:
        This function should not raise any Exceptions.
    """
    if type(y) is not np.ndarray or type(y_hat) is not np.ndarray:
        return None
    if y.all() is None or y_hat.all() is None:
        return None
    if y.shape != y_hat.shape:
        return None
    return np.sqrt(mse_(y, y_hat))


def mae_(y, y_hat):
    """
        Description:
        Calculate the MAE between the predicted output and the real output.
        Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
        Returns:
        mae: has to be a float.
        None if there is a matching dimension problem.
        Raises:
        This function should not raise any Exceptions.
    """
    if type(y) is not np.ndarray or type(y_hat) is not np.ndarray:
        return None
    if y.all() is None or y_hat.all() is None:
        return None
    if y.shape != y_hat.shape:
        return None
    q = 1 / y.shape[0]
    return np.absolute(y_hat - y).sum() * q


def r2score_(y, y_hat):
    """
        Description:
        Calculate the R2score between the predicted output and the output.
        Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
        Returns:
        r2score: has to be a float.
        None if there is a matching dimension problem.
        Raises:
        This function should not raise any Exceptions.
    """
    if type(y) is not np.ndarray or type(y_hat) is not np.ndarray:
        return None
    if y.all() is None or y_hat.all() is None:
        return None
    if y.shape != y_hat.shape:
        return None
    u = y.mean()
    q = np.dot((y_hat - u).T, y_hat - u)
    return 1 - np.dot((y_hat - y).T, y_hat - y) / q
