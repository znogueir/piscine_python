from tester_utils import test_program

path = "whatis.py"

test_program(path, [], "", "")
test_program(path, ["12"], "I'm Even.\n", "")
test_program(path, ["12352625"], "I'm Odd.\n", "")
test_program(
    path, ["whatis"], "", "AssertionError: argument is not an integer\n"
)
test_program(
    path, ["asdg"], "", "AssertionError: argument is not an integer\n"
)
test_program(
    path,
    ["whatis", ""],
    "",
    "AssertionError: more than one argument is provided\n",
)
test_program(
    path,
    ["whatis", "12", "14"],
    "",
    "AssertionError: more than one argument is provided\n",
)
test_program(
    path,
    ["whatis", "asdg", "14"],
    "",
    "AssertionError: more than one argument is provided\n",
)
