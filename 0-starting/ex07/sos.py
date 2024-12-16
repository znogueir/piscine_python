import sys


sys.tracebacklimit = 0


def main(args: list):
    """
    Translates a string into morse code and prints it.
    """
    assert len(args) == 2, "the arguments are bad"

    for c in args[1]:
        assert c.isalnum() or c.isspace(), "the arguments are bad"

    NESTED_MORSE = {
        " ": "/",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
    }

    print(" ".join([NESTED_MORSE[c.lower()] for c in args[1]]))


if __name__ == "__main__":
    main(sys.argv)
