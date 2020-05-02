import numpy as np

def confusion_matrix_(y_true, y_hat, labels=None):
    """
        Compute confusion matrix to evaluate the accuracy of a classification.
        Args:
        y_true:a numpy.ndarray for the correct labels
        y_hat:a numpy.ndarray for the predicted labels
        labels: optional, a list of labels to index the matrix. This may be used to reorder or
        , →
        select a subset of labels. (default=None)
        Returns:
        The confusion matrix as a numpy ndarray.
        None on any error.
        Raises:
        This function should not raise any Exception.
    """
    if labels == None:
        pos_label = np.unique(y_hat)[0]
    else:
        pos_label = labels[0]
    y = np.array(y_true)
    r = np.ones((2,2))
    r[0, 0] = len(y_hat[(y == y_hat) & (y == pos_label)])
    r[0, 1] = len(y_hat[(y == y_hat) & (y != pos_label)])
    r[1, 0] = len(y_hat[(y != y_hat) & (y != pos_label)])
    r[1, 1] = len(y_hat[(y != y_hat) & (y == pos_label)])
    return r
