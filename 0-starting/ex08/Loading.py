from os import get_terminal_size
from time import time


def loading_bar(size: int, prog: float):
    """
    Renders the current prog bar.
    Returns a string.
    """

    size = max(size, 1)
    prog_size = int(size * prog)
    bar = "█" * prog_size + " " * (size - prog_size)

    return bar


def format_time(seconds: float):
    """
    Takes a duration in seconds as parameter.
    Returns it as a string in the following format:
    MM:SS if the duration is under an hour.
    If it is longer, the number of hours is prepended to the format above,
    without limits to the number of digits.
    """

    seconds = int(seconds)

    hours, secs = divmod(seconds, 3600)
    mins, secs = divmod(secs, 60)

    res = f"{f'{int(hours)}:' if hours else ''}{int(mins):02d}:{int(secs):02d}"

    return res


def status_bar(prog: float, i: int, n: int, start: float):
    """
    Calculates the elapsed time, the estimated remaining time,
    and the speed of prog.
    Returns a string."""

    curr_time = time()
    elapsed = curr_time - start
    sp = i / elapsed if i > elapsed else elapsed / i
    unit = "it/s" if i > elapsed else "s/it"
    remaining = format_time(elapsed / prog - elapsed)

    return f" {i}/{n} [{format_time(elapsed)}<{remaining}, {sp:>5.2f}{unit}]"


def ft_tqdm(lst: range):
    """
    Takes a range as a parameter,
    Displays a loading bar according to the range, with the speed
    and estimated remaining time.
    Yields each number in the range.
    """

    cols, _ = get_terminal_size(0)
    n = lst[-1] + 1

    start = time()

    for i in lst:
        prog = i / float(n) if i > 0 else 0

        status = f" 0/{n} [00:00<?, ?it/s]"
        if i > 0:
            status = status_bar(prog, i, n, start)
        bar = loading_bar(cols - len(status) - 6, prog)
        print(f"{int(round(prog * 100)):>3}%|{bar}|{status}\r", end="\r")

        yield i

    status = status_bar(1.0, i + 1, n, start)
    bar = loading_bar(cols - len(status) - 6, 1.0)
    print(f"100%|{bar}|{status}\r", end="\r")
