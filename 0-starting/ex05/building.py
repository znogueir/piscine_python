import sys

sys.tracebacklimit = 0


def print_content(line: str):
    """
    Takes a str as a parameter
    Prints the number of different types of characters in it
    Returns nothing
    """
    types_nb = [0] * 4
    types_comp = [str.isupper, str.islower, str.isspace, str.isdigit]
    for i in range(4):
        types_nb[i] = sum(map(types_comp[i], line))

    print(f"The text contains {len(line)} characters:")
    print(f"{types_nb[0]} upper letters")
    print(f"{types_nb[1]} lower letters")
    print(f"{len(line) - sum(types_nb)} punctuation marks")
    print(f"{types_nb[2]} spaces")
    print(f"{types_nb[3]} digits")


def main(args: list):
    """
    thats the main lol
    """
    assert len(args) <= 2, "more than one argument provided"

    if len(args) < 2:
        print("What is the text to count?")
        line = sys.stdin.readline()
    else:
        line = args[1]

    print_content(line)


if __name__ == "__main__":
    main(sys.argv)
