import sys

if len(sys.argv) < 2:
    print("AssertionError: one argument is required")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif not isinstance(int(sys.argv[1]), int):
    print("AssertionError: argument is not an integer")
else:
    print("I'm Odd." if abs(int(sys.argv[1])) % 2 else "I'm Even.")
