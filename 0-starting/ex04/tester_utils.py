import subprocess
import sys

sys.tracebacklimit = 0

RED = "\033[38;5;196m"
GREEN = "\033[38;5;10m"
R = "\033[0m"


def find_split(exp: str, res: str):
    """
    Takes an expected string and a result string as parameters.
    Returns the index at which they differ.
    """
    for i in range(len(exp)):
        if i > len(res) - 1:
            return i
        if exp[i] != res[i]:
            return i
    return len(exp)


def format_test_result(stream: str, exp: str, res: str):
    """
    Takes an expected string and a result string as parameters,
    Returns a formatted string containing both, with some colors.
    """

    # Im putting these in quotes cause it looks better.
    # also you can see if a string is empty or full of spaces
    exp = f'"{exp}"'
    res = f'"{res}"'

    # I wanted to make the output green until it differs with the
    # expected output, and then red.
    # so im getting the index at which the strings differ here
    ind = find_split(exp, res)

    expected = f'\nExpected {stream}:{GREEN}{" "*4+exp}{R}\n'
    found = f'found: {GREEN}{" "*13+res[:ind]}{RED}{res[ind:]}{R}'

    return expected + found


def assert_test(title: str, out: str, exp: str):
    """
    Takes in a title in parameter, with an output and an
    expected result.
    Checks if they differ, if so, throws an assertion error.
    Prints the results in a nice format.
    """
    assert exp == out, format_test_result("stdout", exp, out)

    print(title)
    print(format_test_result("stdout", exp, out))
    print("====================================================")
    print()


def assert_outputs(title: str, out: str, exp_out: str, err: str, exp_err: str):
    """
    Takes a title in parameter, with the stdout, stderr of a program and
    the expected stdout and expected stdout.
    Checks if they differ, if so, throws an assertion error.
    Prints the results in a nice format.
    """

    assert out == exp_out, format_test_result("stdout", exp_out, out)
    assert err == exp_err, format_test_result("stderr", exp_err, err)

    print(title)
    print(format_test_result("stdout", exp_out, out))
    print(format_test_result("stderr", exp_err, err))
    print("====================================================")
    print()


def test_program(script_path, args, exp_out, exp_err):
    """
    Runs the script/program specified at script_path with args
    Asserts if the outputs correspond to the expected outputs
    Returns nothing.
    """

    r = subprocess.run(
        ["python3"] + [script_path] + args,
        capture_output=True,
        text=True,
    )

    assert_outputs(
        f"Testing program with args: {args}",
        r.stdout,
        exp_out,
        r.stderr,
        exp_err,
    )
