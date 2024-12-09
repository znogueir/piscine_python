def filterstring(cond, it):
    """filter(function or None, iterable) --> filter object

    \rReturn an iterator yielding those items of iterable for which function(item)
    \ris true. If function is None, return the items that are true.
    """
    # Carriage returns in docstring in order to remove the auto indents
    # from my formatter.
    return (x for x in it if (not cond and x) or (cond and cond(x)))
