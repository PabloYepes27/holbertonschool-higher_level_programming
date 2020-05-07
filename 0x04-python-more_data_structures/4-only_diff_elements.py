#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """function that returns a set of common elements in two sets.

    Arguments:
        set_1 {set} -- Set 2
        set_2 {set} -- Set 1

    Returns:
        [type] -- a set of common elements in two sets
    """
    return list((set_1 | set_2) - (set_1 & set_2))
