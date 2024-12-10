from os import get_terminal_size
from time import time


def render_loading_bar(size: int, progress: float):
    """
    Renders the current progress bar.
    Returns a string.
    """

    if size <= 0:
        size = 1

    progress_size = int(size * progress)
    bar = "=" * progress_size + " " * (size - progress_size)

    return bar


def format_time_durations(seconds: float):
    seconds = int(seconds)

    hours = seconds // 3600
    mins = seconds // 60
    secs = seconds % 60

    res = f"{int(mins):02d}:{int(secs):02d}"
    if hours:
        mins = (seconds % 3600) * 60
        res = f"{int(hours):02d}:{res}"

    return res


def render_time_estimations(progress: float, i: int, n: int, start: float):
    """
    Calculates the elapsed time, the estimated remaining time,
    and the speed of progress.
    Returns a string."""
    if i == 0:
        return f" 0/{n} [00:00<?,  ?it/s]"

    curr_time = time()
    elapsed = curr_time - start
    speed = i / elapsed
    unit = "it/s"
    if speed < 1:
        speed = elapsed / i
        unit = "s/it"

    elapsed_str = format_time_durations(elapsed)
    remaining_str = format_time_durations(elapsed / progress - elapsed)
    status = f" {i}/{n} [{elapsed_str}<{remaining_str}, {speed:>5.2f}{unit}]"

    return status


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
        progress = i / float(n) if i > 0 else 0

        status = render_time_estimations(progress, i, n, start)
        bar = render_loading_bar(cols - len(status) - 6, progress)
        print(f"{int(round(progress * 100)):>3}%|{bar}|{status}\r", end="\r")

        yield i

    status = render_time_estimations(1.0, i + 1, n, start)
    bar = render_loading_bar(cols - len(status) - 6, 1.0)
    print(f"100%|{bar}|{status}\r", end="\r")
