p = {
    type(None): ["Nothing:", None],
    float: ["Cheese: ", float("NaN")],
    bool: ["Fake:", False],
    int: ["Zero:", 0],
    str: ["Empty:", ""],
}


def NULL_not_found(obj: any) -> int:
    t = type(obj)
    if t in p and obj == p[t][1] or (isinstance(obj, float) and obj != obj):
        print(p[t][0], obj, t)
        return 0
    print("Type not Found")
    return 1
