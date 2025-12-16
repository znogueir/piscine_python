import sys
import numpy


def ft_load(path: str) -> array:
    """
    Loads an image file from path, prints its
    format, and the RGB values of its pixels as an array.

    :param path: the path to the image file
    :type path: str
    :return: the RGB values of the pixels
    :rtype: array
    """

    try:
        with open(path, "r") as f:
            contents = f.read()

        # print the shape of the img array (h x l x 3)
        # print the img as a numpy array of (h x l x 3)
        return contents

    except Exception as e:
        print(str(e), file=sys.stderr)

    return []
