import sys
import numpy


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices the array family from start to end.

    :param family: a list of elements
    :type family: list
    :param start: the start of the slice
    :type start: int
    :param end: the end of the slice
    :type end: int
    :return: the result of the slice
    :rtype: list
    """

    try:
        print(f"My shape is : {numpy.array(family).shape}")
        res = family[start:end]
        print(f"My new shape is : {numpy.array(res).shape}")
        return res

    except Exception as e:
        print(str(e), file=sys.stderr)

    return []
