def filterstring(it: list, cond=None):
    for x in it:
        if not cond:
            if x:
                yield x
        elif cond(x):
            yield x
