import sys
import numpy as np

def ft_invert(arr: np.ndarray) -> np.ndarray:
    """
    Takes in an img as an array and inverts its colors.

    :param arr: the img as an array
    :type arr: numpy.ndarray
    :return: the inverted RGB values
    :rtype: numpy.ndarray
    """

    h, w, c = arr.shape
    res = np.empty((h, w, c), dtype=arr.dtype)

    for i in range(h):
        for j in range(w):
            res[i, j] = [255 - c for c in arr[i, j]]

    return res


def ft_red(arr: np.ndarray) -> np.ndarray:
    """
    Takes in an img as an array and excludes the G and B channels.

    :param arr: the img as an array
    :type arr: numpy.ndarray
    :return: the transformed img
    :rtype: numpy.ndarray
    """

    h, w, c = arr.shape
    res = np.empty((h, w, c), dtype=arr.dtype)

    for i in range(h):
        for j in range(w):
            res[i, j] = [arr[i, j, 0], 0, 0]

    return res

def ft_green(arr: np.ndarray) -> np.ndarray:
    """
    Takes in an img as an array and excludes the R and B channels.

    :param arr: the img as an array
    :type arr: numpy.ndarray
    :return: the transformed img
    :rtype: numpy.ndarray
    """

    h, w, c = arr.shape
    res = np.empty((h, w, c), dtype=arr.dtype)

    for i in range(h):
        for j in range(w):
            res[i, j] = [0, arr[i, j, 1], 0]

    return res


def ft_blue(arr: np.ndarray) -> np.ndarray:
    """
    Takes in an img as an array and excludes R and G channels.

    :param arr: the img as an array
    :type arr: numpy.ndarray
    :return: the transformed img
    :rtype: numpy.ndarray
    """

    h, w, c = arr.shape
    res = np.empty((h, w, c), dtype=arr.dtype)

    for i in range(h):
        for j in range(w):
            res[i, j] = [0, 0, arr[i, j, 2]]

    return res


def ft_grey(arr: np.ndarray) -> np.ndarray:
    """
    Takes in an img as an array and converts it to grey scale.

    :param arr: the img as an array
    :type arr: numpy.ndarray
    :return: the grey scale img
    :rtype: numpy.ndarray
    """

    return arr
