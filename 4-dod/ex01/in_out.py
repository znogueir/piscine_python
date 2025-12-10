def square(x: int | float) -> int | float:
    """Return the square of x"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the exponentiation of x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Outer function
    Define inner function, calls and returns it
    """
    count = 0

    def inner() -> float:
        """
        Inner function

        nonlocal used to modify the outer variable
        If first time: assign x to count
        Else: use the return of last call
        """
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count
    return inner
