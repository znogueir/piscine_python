def filterstring(cond, it):
    """TODO"""
    for x in it:
        if not cond and x or cond and cond(x):
            yield x
