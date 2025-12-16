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

    return 255 - arr


def ft_red(arr: np.ndarray) -> np.ndarray:
    """
    Takes in an img as an array and excludes the G and B channels.

    :param arr: the img as an array
    :type arr: numpy.ndarray
    :return: the transformed img
    :rtype: numpy.ndarray
    """

    res = arr.copy()
    res[:, :, 1:] = 0
    return res

def ft_green(arr: np.ndarray) -> np.ndarray:
    """
    Takes in an img as an array and excludes the R and B channels.

    :param arr: the img as an array
    :type arr: numpy.ndarray
    :return: the transformed img
    :rtype: numpy.ndarray
    """

    res = arr.copy()
    res[:, :, ::2] = 0
    return res


def ft_blue(arr: np.ndarray) -> np.ndarray:
    """
    Takes in an img as an array and excludes R and G channels.

    :param arr: the img as an array
    :type arr: numpy.ndarray
    :return: the transformed img
    :rtype: numpy.ndarray
    """

    res = arr.copy()
    res[:, :, :2] = 0
    return res


def ft_grey(arr: np.ndarray) -> np.ndarray:
    """
    Takes in an img as an array and converts it to grey scale.

    :param arr: the img as an array
    :type arr: numpy.ndarray
    :return: the grey scale img
    :rtype: numpy.ndarray
    """

    res = np.dot(arr, [0.299, 0.587, 0.114]) # this results in a 2d array
    # convert to int
    res = np.clip(np.round(res), 0, 255).astype(np.uint8)
    # convert it back into 3 color channels before returning
    return np.stack((res, res, res), axis=-1)
