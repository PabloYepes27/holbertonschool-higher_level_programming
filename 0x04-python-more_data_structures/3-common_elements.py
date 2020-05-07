#!/usr/bin/python3
def common_elements(set_1, set_2):
    """function that returns a set of common elements in two sets.

    Arguments:
        set_1 {set} -- Set 2
        set_2 {set} -- Set 1

    Returns:
        [type] -- a set of common elements in two sets
    """
    # return list(elem for elem in set_1 if elem in set_2)
    return list(set_1 & set_2)
