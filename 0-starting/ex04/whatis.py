import sys

sys.tracebacklimit = 0  # to limit the error prints to most recent error msg


def whatis(args: list):
    if len(args) < 2:
        return

    assert len(args) == 2, "more than one argument is provided"
    try:
        n = int(args[1])
    except ValueError:
        n = None

    assert n is not None, "argument is not an integer"

    print("I'm Odd." if n % 2 else "I'm Even.")


if __name__ == "__main__":
    whatis(sys.argv)
