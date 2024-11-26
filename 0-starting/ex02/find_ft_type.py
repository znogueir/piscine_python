p = {list: "List :", tuple: "Tuple :", set: "Set :", dict: "Dict :"}


def all_thing_is_obj(object: any) -> int:
    t = type(object)
    if t in p:
        print(p[t], t)
    elif isinstance(object, str):
        print(object, "is in the kitchen :", str)
    else:
        print("Type not found")
    return 42
