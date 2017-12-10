import tarfile
import numpy as np
import pandas as pd

def get_images():

    """Get the fashion-mnist images.

    Returns
    -------
    (x_train, x_test) : tuple of uint8 arrays
        Grayscale image data with shape (num_samples, 28, 28)
    (y_train, y_test) : tuple of uint8 arrays
        Labels (integers in range 0-9) with shape (num_samples,)

    Examples
    --------
    >>> from reader import get_images
    >>> (x_train, y_train), (x_test, y_test) = get_images() 

    Notes
    -----
    The data is split into train and test sets as described in the original paper [1].

    References
    ----------
    1. Xiao H, Rasul K, Vollgraf R. Fashion-MNIST: a Novel Image Dataset for 
    Benchmarking Machine Learning Algorithms. CoRR [Internet]. 2017;abs/1708.07747.
    Available from: http://arxiv.org/abs/1708.07747
    """

    with tarfile.open('data.tar.gz', 'r') as f:
        f.extractall()

    df_train = pd.read_csv('fashion_mnist_train.csv')
    df_test = pd.read_csv('fashion_mnist_test.csv')

    x_train = df_train.drop('label', axis=1).as_matrix().astype(np.uint8)
    y_train = df_train['label'].as_matrix().astype(np.uint8)
    x_test = df_test.drop('label', axis=1).as_matrix().astype(np.uint8)
    y_test = df_test['label'].as_matrix().astype(np.uint8)

    return (x_train, y_train), (x_test, y_test)
