from tester_utils import test_program


path = "sos.py"

# no args
test_program(path, [], "", "AssertionError: the arguments are bad\n")
# non alphanumerical chars
test_program(path, ["h$llo"], "", "AssertionError: the arguments are bad\n")
# same
test_program(path, ["@*)&@"], "", "AssertionError: the arguments are bad\n")
# same
test_program(path, ["bonj0ur."], "", "AssertionError: the arguments are bad\n")
# too many args
test_program(path, ["", ""], "", "AssertionError: the arguments are bad\n")


# valid input:

test_program(path, [""], "\n", "")
test_program(path, ["sos"], "... --- ...\n", "")
test_program(path, ["SOS"], "... --- ...\n", "")  # we dont care about case
test_program(path, ["bonj0ur"], "-... --- -. .--- ----- ..- .-.\n", "")
test_program(
    path, ["Hello World"], ".... . .-.. .-.. --- / .-- --- .-. .-.. -..\n", ""
)
test_program(
    path,
    [" h3110 w0r1d "],
    "/ .... ...-- .---- .---- ----- / .-- ----- .-. .---- -.. /\n",
    "",
)
