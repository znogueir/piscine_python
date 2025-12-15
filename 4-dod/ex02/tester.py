from callLimit import callLimit


@callLimit(0)
def h():
    print("h()")


@callLimit(2)
def j():
    print("j()")


@callLimit(1)
def k():
    print("k()")


for i in range(2):
    h()
    j()
    k()
