import numpy as np

def accuracy_score_(y, y_hat):
    """
        Compute the accuracy score.
        Args:
        y:a numpy.ndarray for the correct labels
        y_hat:a numpy.ndarray for the predicted labels
        Returns:
        The accuracy score as a float.
        None on any error.
        Raises:
        This function should not raise any Exception.
    """
    tr = len(y_hat[(y == y_hat)])
    l = len(y_hat)
    return tr / l

def precision_score_(y, y_hat, pos_label=1):
    """
        Compute the precision score.
        39Args:
        y:a numpy.ndarray for the correct labels
        y_hat:a numpy.ndarray for the predicted labels
        pos_label: str or int, the class
        on which to report the precision_score (default=1)
        Returns:
        The precision score as a float.
        None on any error.
        Raises:
        This function should not raise any Exception.
    """
    tp = len(y_hat[(y == y_hat) & (y == pos_label)])
    tn = len(y_hat[(y == y_hat) & (y != pos_label)])
    fp = len(y_hat[(y != y_hat) & (y != pos_label)])
    fn = len(y_hat[(y != y_hat) & (y == pos_label)])
    return tp / (tp + fp)

def recall_score_(y, y_hat, pos_label=1):
    """
        Compute the recall score.
        Args:
        y:a numpy.ndarray for the correct labels
        y_hat:a numpy.ndarray for the predicted labels
        pos_label: str or int, the class
        on which to report the precision_score (default=1)
        Returns:
        The recall score as a float.
        None on any error.
        Raises:
        This function should not raise any Exception.
    """
    tp = len(y_hat[(y == y_hat) & (y == pos_label)])
    tn = len(y_hat[(y == y_hat) & (y != pos_label)])
    fp = len(y_hat[(y != y_hat) & (y != pos_label)])
    fn = len(y_hat[(y != y_hat) & (y == pos_label)])
    return tp / (tp + fn)

def f1_score_(y, y_hat, pos_label=1):
    """
        Compute the f1 score.
        Args:
        y:a numpy.ndarray for the correct labels
        y_hat:a numpy.ndarray for the predicted labels
        pos_label: str or int, the class on
        which to report the precision_score (default=1)
        Returns:
        The f1 score as a float.
        None on any error.
        Raises:
        This function should not raise any Exception.
    """
    p = precision_score_(y, y_hat, pos_label)
    r = recall_score_(y, y_hat, pos_label)
    return (2 * p * r) / (p + r)
