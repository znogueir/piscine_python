import sys
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(img: np.ndarray) -> np.ndarray:
    """
    Zooms on some part of an image (and puts
    it in grey scale).

    :param img: the img to zoom on
    :type img: numpy.ndarray
    :return: the zoomed in img
    :rtype: numpy.ndarray
    """

    try:
        # slicing the image ("zooming")
        img = img[100:500, 450:850]
        # changing to grey scale
        img = np.dot(img, [0.299, 0.587, 0.114])

        print(f"The shape of the image is : (400, 400, 1) or {img.shape}")
        print(img)

        return img

    except Exception as e:
        print(str(e), file=sys.stderr)

    return None


def transpose_2d(arr: np.ndarray) -> np.ndarray:
    """
    Transposes a 2 dimensional array.

    :param arr: the arr to transpose
    :type arr: numpy.ndarray
    :return: the transposed arr
    :rtype: numpy.ndarray
    """

    if arr.ndim != 2:
        raise ValueError("Expected a 2D array")

    h, w = arr.shape
    res = np.empty((w, h), dtype=arr.dtype)

    for i in range(h):
        for j in range(w):
            res[j, i] = arr[i, j]

    return res


def rotate(img: np.ndarray) -> np.ndarray:
    """
    Rotates an image.

    :param img: the img to rotate
    :type img: numpy.ndarray
    :return: the rotated img
    :rtype: numpy.ndarray
    """

    try:
        img = transpose_2d(img)

        print(f"New shape after Transpose: {img.shape}")
        print(img)

        return img

    except Exception as e:
        print(str(e), file=sys.stderr)

    return None


def main():
    """
    main function.
    Loads an img and zooms on it + dispays it.
    """

    img = ft_load("animal.jpeg")
    if img is None:
        print("Error: Encountered issue during load.", file=sys.stderr)
        return 1

    zoomed_img = zoom(img)
    if zoomed_img is None:
        print("Error: Encountered issue during zoom.", file=sys.stderr)
        return 1

    rotated_img = rotate(zoomed_img)
    if rotated_img is None:
        print("Error: Encountered issue during rotation.", file=sys.stderr)
        return 1

    plt.imshow(rotated_img, cmap="gray")
    plt.show()

    return 0


if __name__ == "__main__":
    sys.exit(main())
