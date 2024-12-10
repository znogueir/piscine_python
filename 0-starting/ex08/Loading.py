import os
import time


def render_percentage(progress: float):
    """
    Calcualtes the current progress as percentage.
    Returns a string.
    """
    percentage = int(progress * 100)
    percentage_str = str(percentage)
    percentage_str = " " * (3 - len(percentage_str)) + percentage_str

    return percentage_str


def render_loading_bar(size: int, progress: float):
    """
    Calculates the current progress bar.
    Returns a string.
    """
    if size <= 0:
        size = 1

    progress_size = int(size * progress)
    loading_bar = "=" * progress_size + " " * (size - progress_size)

    return loading_bar


def render_time_estimations(i: int, n: int, start_time: float, curr_time: float):
    """
    Calculates the elapsed time, the estimated duration,
    and the speed of progress.
    Returns a string."""
    elapsed = 0
    duration = None
    speed_str = "?it/s"  # or s/it if ratio < 1.0
    elapsed_str = "00:00"

    status = f" {i + 1}/{n} [{elapsed_str}<{duration}, {speed_str}]"

    return status


def ft_tqdm(lst: range):
    """
    Takes a range as a parameter,
    Displays a loading bar according to the range, with the speed
    and estimated end time.
    Yields each number in the range.
    """

    cols, _ = os.get_terminal_size(0)
    n = lst[-1] + 1

    start_time = time.time()
    curr_time = None
    elapsed = 0

    for i in lst:
        progress = (i + 1) / float(n)

        if curr_time is not None:
            elapsed = curr_time - start_time
        curr_time = time.time()

        # render the 3 main elements of the bar
        percentage = render_percentage(progress)
        status = render_time_estimations(i, n, start_time, elapsed)
        loading_bar = render_loading_bar(cols - len(status) - 6, progress)

        # display the complete loading bar
        print(
            f"{percentage}%|{loading_bar}|{status}\r",
            end="\r",
        )

        # yield current value ?
        yield i
