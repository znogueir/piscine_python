import sys


def process_input(s: str):
    """
    process_input(s: str):
    Takes a string as a parameter.
    Returns the number of different character types in it.
    """

    content = [0] * 6

    for c in s:
        content[0] += 1
        if c.isupper():
            content[1] += 1
        elif c.islower():
            content[2] += 1
        elif c == " " or c == "\n":
            content[4] += 1
        elif c.isdigit():
            content[5] += 1
        else:
            content[3] += 1

    return content


def print_content(res: list):
    """
    print_content(res: list)
    Takes a list as a parameter
    Prints the content of the list formatted, returns nothing
    """
    print(f"The text contains {res[0]} characters:")
    print(res[1], "upper letters")
    print(res[2], "lower letters")
    print(res[3], "punctuation marks")
    print(res[4], "spaces")
    print(res[5], "digits")


def main(args: list):
    """
    Thats the main lol.
    """
    assert len(args) <= 2, "more than one argument provided"

    s = input("What is the text to count?\n") if len(args) == 1 else args[1]
    print(s, "end")
    print_content(process_input(s))


if __name__ == "__main__":
    main(sys.argv)
