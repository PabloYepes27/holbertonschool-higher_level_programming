#!/usr/bin/python3
def uniq_add(my_list=[]):
    """function that adds all unique integers in a list
    (only once for each integer)

    Keyword Arguments:
        my_list {list} -- [list of integers] (default: {[]})

    Returns:
        [type] -- [sum of elements of the list]
    """
    return sum(set(my_list))
