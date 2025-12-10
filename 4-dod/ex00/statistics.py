def mean(*args: any):
    """ Return the mean of a list """
    return sum(args) / len(args)


def median(*args: any):
    """
    Calculate the median of the tuple

    // : double division operator, divides and the floor int
    (can't use indexing if float)
    """
    sorted_args = sorted(args)
    size = len(sorted_args)
    if size % 2 == 1:
        return sorted_args[size // 2]
    else:
        return (sorted_args[size // 2 - 1] + sorted_args[size / 2]) / 2.0


def quartile(*args: float) -> list[float] | None:
    """Calculate the quartile of the tuple (25 and 75%)"""

    data = sorted(args)
    n = len(data)

    middle_index_floor = (n + 1) // 2
    lower_half = data[:middle_index_floor]
    upper_half = data[middle_index_floor - 1:]

    Q1 = median(*lower_half)
    Q3 = median(*upper_half)

    return [Q1, Q3]


def var(*args: float) -> float:
    """
        Calculate the variance of the tuple

        Variance: a statistical measurement of how large of
        a spread there is within a data set
    """
    mu = mean(*args)
    n = len(args)

    squared_differences_sum = sum((x - mu) ** 2 for x in args)
    return squared_differences_sum / n


def std(*args: any):
    """
        Calculate the standard variation of the tuple

        std: Standard deviation is a statistical measure
        that quantifies the amount of variation or dispersion
        of a set of data values from their mean

        The standard deviation is calculated as the square
        root of the variance
    """
    variance = var(*args)
    return variance ** 0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
        Print the result of the given function with
        the given args
    """

    if not kwargs:
        return

    try:

        for k, val in kwargs.items():
            if not args:
                print("ERROR")
            elif val == "mean":
                print(f"mean : {mean(*args)}")
            elif val == "median":
                print(f"median : {median(*args)}")
            elif val == "quartile":
                print(f"quartile : {quartile(*args)}")
            elif val == "std":
                print(f"std : {std(*args)}")
            elif val == "var":
                print(f"var : {var(*args)}")

    except Exception as err:
        print(f"ERROR: {err}")
