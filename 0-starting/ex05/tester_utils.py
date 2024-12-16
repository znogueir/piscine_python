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

    # Im putting these in quotes if they already are strings, this
    # way we can better differentiate outputs.
    exp = f'"{exp}"' if isinstance(exp, str) else str(exp)
    res = f'"{res}"' if isinstance(res, str) else str(res)

    # I wanted to make the output green until it differs with the
    # expected output, and then red.
    # so im getting the index at which the strings differ here
    ind = find_split(exp, res)

    expected = (
        f'\nExpected{stream}:{GREEN}{" "*(4 if stream else 11)+exp}{R}\n'
    )
    found = f'Found: {GREEN}{" "*13+res[:ind]}{RED}{res[ind:]}{R}'

    return expected + found


def assert_tests(
    title: str, out: str, exp_out: str, err: str = None, exp_err: str = None
):
    """
    Parameters:
    Title of the test, Output, Expected output, Error output (Optional),
    Expected error output (Optional)

    Checks if the outputs differ from the expected ones, if so,
    throws an assertion error.
    Prints the results in a nice format.
    """

    stdout = "" if err is None and exp_err is None else " stdout"

    print(title)
    assert out == exp_out, format_test_result(stdout, exp_out, out)
    if err is not None and exp_err is not None:
        assert err == exp_err, format_test_result(" stderr", exp_err, err)

    print(format_test_result(stdout, exp_out, out))
    if err is not None and exp_err is not None:
        print(format_test_result(" stderr", exp_err, err))
    print("==========================================================")
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

    assert_tests(
        f"Testing program with args: {args}",
        r.stdout,
        exp_out,
        r.stderr,
        exp_err,
    )
