from filterstring import filterstring
from tester_utils import test_program, assert_tests

# ========== testing the function itself first ===========
assert_tests("Comparing Docstrings", filterstring.__doc__, filter.__doc__)
assert_tests(
    f"filter function with args: {None, [1, 0, 0, 1, 1]}",
    [x for x in filterstring(None, [1, 0, 0, 1, 1])],
    [x for x in filter(None, [1, 0, 0, 1, 1])],
)
assert_tests(
    f"filter function with args: {None, [True, False, False, True, True]}",
    [x for x in filterstring(None, [True, False, False, True, True])],
    [x for x in filter(None, [True, False, False, True, True])],
)
assert_tests(
    f"filter function with args: {None, ["", "blabla", "hehe", ""]}",
    [
        x
        for x in filterstring(
            None,
            ["", "blabla", "hehe", ""],
        )
    ],
    [
        x
        for x in filter(
            None,
            ["", "blabla", "hehe", ""],
        )
    ],
)
assert_tests(
    f"filter function with args: {'lambda x: x == 0', [1, 0, 0, 1, 1]}",
    [x for x in filterstring(lambda x: x == 0, [1, 0, 0, 1, 1])],
    [x for x in filter(lambda x: x == 0, [1, 0, 0, 1, 1])],
)
list = [
    "4.2",
    "42042",
    "42 students are",
    "im 24",
    "hello world",
    "4242",
    "the best. #42",
]
assert_tests(
    f"filter function with args: {'lambda x: x.count("42") == 1', list}",
    [x for x in filterstring(lambda x: x.count("42") == 1, list)],
    [x for x in filter(lambda x: x.count("42") == 1, list)],
)


# =============== testing the program now ================
path = "ft_filter.py"

# 2nd arg (N) is not an int
test_program(
    path,
    ["3", "Hello the World"],
    "",
    "AssertionError: the arguments are bad\n",
)
# no args
test_program(path, [], "", "AssertionError: the arguments are bad\n")
# missing N
test_program(
    path, ["missing an arg"], "", "AssertionError: the arguments are bad\n"
)
# too many args
test_program(
    path,
    ["N is here", "4", "but too many args"],
    "",
    "AssertionError: the arguments are bad\n",
)
# not an int
test_program(
    path,
    ["Enough args but not an int", "not an int"],
    "",
    "AssertionError: the arguments are bad\n",
)
# not an int and too many args
test_program(
    path,
    ["a string", "another string", "too many args"],
    "",
    "AssertionError: the arguments are bad\n",
)

# correct args
test_program(
    path,
    ["Hello the World", "4"],
    "['Hello', 'World']\n",
    "",
)
test_program(
    path,
    ["Hello the World", "99"],
    "[]\n",
    "",
)
test_program(
    path,
    ["a string", "2"],
    "['string']\n",
    "",
)
test_program(
    path,
    ["1 4444 22 55555 333 22 4444 666666 999999999 1 22", "4"],
    "['4444', '55555', '4444', '666666', '999999999']\n",
    "",
)
