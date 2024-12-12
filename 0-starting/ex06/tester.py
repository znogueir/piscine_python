from filterstring import filterstring
from tester_utils import test_program, format_test_result

assert filterstring.__doc__ == filter.__doc__, format_test_result(
    "", filter.__doc__, filterstring.__doc__
)

# test the function itself first

# test the program now
path = "ft_filter.py"

test_program(path, [], "", "")
