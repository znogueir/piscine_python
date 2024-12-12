def filterstring(cond, it):
    return (x for x in it if (not cond and x) or (cond and cond(x)))


# forced to put this here since the docstring is too long to be indented
# and results in a fail when checking the norm with flake8
filterstring.__doc__ = """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
