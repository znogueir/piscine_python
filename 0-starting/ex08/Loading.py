from os import get_terminal_size
from time import time


def loading_bar(i: int, n: int, total_bar_len: int):
    """
    Renders the current prog bar.
    Returns a string.
    """

    gradient = " ▏▎▍▌▌▊█"
    fract = i / n

    # (in case the terminal is too small, we set the length to 1,
    # which is the minimum length for the bar)
    total_bar_len = max(total_bar_len, 1)
    bar_len = fract * total_bar_len
    filled_len = int(bar_len)
    rem_idx = int((bar_len - filled_len) * 8)

    # now we compose the loading bar
    bar = gradient[-1] * filled_len
    if i < n:
        bar += f"{gradient[rem_idx]}{' '*(total_bar_len - filled_len - 1)}"

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
    # here if the speed is too small, to be precise if it is
    # lower that 1.0 it/s, it is instead displayed in s/it.
    # so we swap the operands.
    # PS: this function is only called if i > 0 so we are safe ;)
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

    n = len(lst)
    if n == 0:
        print("0it [00:00, ?it/s]")
        return

    cols, _ = get_terminal_size(0)
    start = time()

    for i in lst:
        prog = i / float(n) if i > 0 else 0

        status = f" 0/{n} [00:00<?, ?it/s]"
        if i > 0:
            status = status_bar(prog, i, n, start)
        bar = loading_bar(i, n, cols - len(status) - 6)
        print(f"{int(round(prog * 100)):>3}%|{bar}|{status}\r", end="\r")

        yield i

    # we print the bar one last time at the end, since the range stops
    # one item before its length and we started at 0.
    status = status_bar(1.0, n, n, start)
    bar = loading_bar(n, n, cols - len(status) - 6)
    print(f"100%|{bar}|{status}\r", end="\r")
