from tester_utils import test_program

subject_example = """Python 3.0, released in 2008, was a major
revision that is not completely backward-compatible with earlier
versions. Python 2 was discontinued with version 2.7.18 in 2020."""
subject_result = """The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
"""

hello_return = """Hello World!
"""
hello_return_result = """The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
"""

hello_no_return = """Hello World!"""
hello_no_return_result = """The text contains 12 characters:
2 upper letters
8 lower letters
1 punctuation marks
1 spaces
0 digits
"""

path = "building.py"
test_program(path, [subject_example], subject_result, "")
test_program(path, [hello_return], hello_return_result, "")
test_program(path, [hello_no_return], hello_no_return_result, "")
