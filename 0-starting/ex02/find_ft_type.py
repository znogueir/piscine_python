p = {list: "List :", tuple: "Tuple :", set: "Set :", dict: "Dict :"}


def all_thing_is_obj(object: any) -> int:
    for t in p:
        if isinstance(object, t):
            print(p[t], type(object))
            return 42
    if isinstance(object, str):
        print(object, "is in the kitchen :", type(object))
    else:
        print("Type not found")
    return 42
