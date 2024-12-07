import sys
from filterstring import filterstring

sys.tracebacklimit = 0


def main(args: list):
    """Prints the words of a string that are longer than N"""
    assert len(args) == 3, "the arguments are bad"

    n = None
    try:
        n = int(args[2])
    except ValueError:
        n = None
    assert n is not None, "the arguments are bad"

    s = args[1].split()

    print([x for x in filterstring(lambda x: len(x) >= n, s)])


if __name__ == "__main__":
    main(sys.argv)
