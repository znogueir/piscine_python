import sys


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    Calculates the bmi for each values in height and weight.
    Returns an array of bmis.

    :param height: a list of heights in meters
    :type height: list[int | float]
    :param weight: a list of weights in kg
    :type weight: list[int | float]
    :return: a list of the calculated bmis
    :rtype: list[int | float]
    """

    try:
        # check if height and weight are the same length
        if len(height) != len(weight):
            raise ValueError("height and weight should be the same length.")

            # check if height is a list of floats or ints
        if not all(type(h) in (int, float) for h in height):
            raise TypeError("height should be a list of floats or ints.")

            # check if weight is a list of floats or ints
        if not all(type(w) in (int, float) for w in weight):
            raise TypeError("weight should be a list of floats or ints.")

        return [w / (h * h) for h, w in zip(height, weight)]

    except Exception as e:
        print(str(e), file=sys.stderr)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    For each value in bmi, checks if it is higher than limit.
    Returns an array containing each result.

    :param bmi: a list of bmis
    :type bmi: list[int | float]
    :param limit: the limit that the bmis should respect
    :type limit: int
    :return: a list of booleans (bmi higher than limit)
    :rtype: list[bool]
    """

    try:
        # check if bmi is empty
        if len(bmi) == 0:
            raise ValueError("bmi should not be empty.")

        # check if bmi is a list of floats or int
        if not all(type(b) in (int, float) for b in bmi):
            raise TypeError("bmi should be a list of floats or ints.")

        return [w > limit for w in bmi]

    except Exception as e:
        print(str(e), file=sys.stderr)
        return []
