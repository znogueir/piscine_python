import sys
import numpy
from PIL import Image


def ft_load(path: str) -> numpy.ndarray:
    """
    Loads an image file from path, prints its
    format, and the RGB values of its pixels as an array.

    :param path: the path to the image file
    :type path: str
    :return: the RGB values of the pixels
    :rtype: array
    """

    try:
        if not path:
            raise ValueError("path is empty.")

        img = Image.open(path)
        if not img:
            raise ValueError("could not load image.")

        img = numpy.array(img)
        # print(f"The shape of the image is : {img.shape}")

        return img

    except Exception as e:
        print(str(e), file=sys.stderr)

    return None
