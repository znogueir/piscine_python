from typing import Any


def all_thing_is_obj(object: Any) -> int:
    t = type(object)
    if t in [list, tuple, set, dict]:
        print(str(t).split("'")[1].capitalize(), ":", t)
    elif isinstance(object, str):
        print(object, "is in the kitchen :", str)
    else:
        print("Type not found")
    return 42
