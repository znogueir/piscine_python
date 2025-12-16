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

        print(f"New shape after slicing : (400, 400, 1) or {img.shape}")
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
    print(img)

    zoomed_img = zoom(img)
    if not zoomed_img:
        print("Error: Encountered issue during zoom.", file=sys.stderr)
        return 1

    plt.imshow(zoomed_img, cmap="gray")
    plt.show()

    return 0


if __name__ == "__main__":
    sys.exit(main())
