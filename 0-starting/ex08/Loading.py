import os


def ft_tqdm(lst: range):
    """
    ft_tqdm(lst: range)

    Takes a range as a parameter,
    Displays a loading bar according to the range, with the speed
    and estimated end time.
    """
    # get the length of the terminal
    columns, _ = os.get_terminal_size(0)

    # get the number of elements in the range
    nbr_of_elems = lst[-1] + 1

    percentage = 0  # "000%"
    loading_bar = ""  # "|<progress = chars followed by spaces>|"
    status_infos = ""
    elapsed_time = "--:--"
    estimated_duration = "--:--"
    speed = "0.00it/s"  # or s/it if ratio < 1.0

    for i in lst:
        # compose the percentage string
        percentage = int(round((i + 1) / nbr_of_elems * 100))
        percentage_str = str(percentage)
        percentage_str = " " * (3 - len(percentage_str)) + percentage_str

        # compose the status string
        status_infos = (
            f" {i + 1}/{nbr_of_elems} [{elapsed_time}<{estimated_duration}, {speed}]"
        )

        # get the length of the loading bar :
        loading_bar_length = columns - len(status_infos) - 6
        if loading_bar_length <= 0:
            loading_bar_length = 1

        # compute progress bar
        progress_bar_length = int(percentage / 100.0 * loading_bar_length)

        # assemble loading bar
        loading_bar = "=" * progress_bar_length + " " * (
            loading_bar_length - progress_bar_length
        )

        # display the complete loading bar
        print(
            f"{percentage_str}%|{loading_bar}|{status_infos}\r",
            end="\r",
        )

        # yield current value ?
        yield i
