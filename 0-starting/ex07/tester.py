from tester_utils import test_program


path = "sos.py"

test_program(path, [], "", "AssertionError: the arguments are bad\n")
