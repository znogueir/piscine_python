
def callLimit(limit: int):
    """ Decorator factory
        Retrieve the decorator argument
    """
    count = 0

    def callLimiter(function):
        """ 'Real' decorator
            Receive the function to call
        """

        def limit_function(*args: any, **kwds: any):
            """
                Replace main function (f or g)
                The one called by the script each time
                we exec f or g
            """
            try:
                nonlocal count
                if count < limit:
                    count += 1
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function
    return callLimiter
