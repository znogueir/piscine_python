import subprocess
import sys

sys.tracebacklimit = 0

RED = "\033[38;5;196m"
ORANGE = "\033[38;5;202m"
YELLOW = "\033[38;5;220m"
GREEN = "\033[38;5;10m"
BLUE = "\033[38;5;45m"
R = "\033[0m"


def format_test_result(col: str, stream: str, exp: str, res: str):
    exp = f'"{exp}"'
    res = f'"{res}"'
    expected = f'{col}\nExpected {stream}:{" "*4+exp}\n'
    found = f'found: {" "*13+res}{R}'
    return expected + found


def test_program(script_path, args, exp_out, exp_err):
    r = subprocess.run(
        ["python3"] + [script_path] + args,
        capture_output=True,
        text=True,
    )

    assert r.stdout == exp_out, format_test_result(
        RED, "stdout", exp_out, r.stdout
    )
    assert r.stderr == exp_err, format_test_result(
        RED, "stderr", exp_err, r.stderr
    )

    print("Test passed with", args)
    print(format_test_result(GREEN, "stdout", exp_out, r.stdout))
    print(format_test_result(GREEN, "stdout", exp_err, r.stderr))
    print("====================================================")
    print()


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
