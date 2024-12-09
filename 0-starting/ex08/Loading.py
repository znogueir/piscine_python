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
    nbr_of_elems = lst[-1] + 1
    # get the length of the loading bar :
    # total length - eta string - 5
    # if the length of loading bar is <= 0:
    # set it to 1
    percentage = ""  # "000%"
    loading_bar = ""  # "|<progress = chars followed by spaces>|"
    status_infos = ""  # " <i + 1/nbr of elems [time elapsed<estimated duration, <1 or 2 spaces><speed>it/s or s/it]"

    for i in lst:
        # compose the percentage string
        percentage = int(round((i + 1) / nbr_of_elems * 100))
        # compose the eta string
        # pass
        # output the complete loading bar
        print(f"{percentage}%|{i}", end="\r")
        yield i
