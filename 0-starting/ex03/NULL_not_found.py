p = {
    type(None): ["Nothing:", None],
    float: ["Cheese: ", float("NaN")],
    bool: ["Fake:", False],
    int: ["Zero:", 0],
    str: ["Empty:", ""],
}


def NULL_not_found(object: any) -> int:
    t = type(object)
    if t in p and object == p[t][1] or (isinstance(object, float) and object != object):
        print(p[t][0], object, t)
        return 0
    print("Type not Found")
    return 1
