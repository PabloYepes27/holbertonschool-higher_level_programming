#!/usr/bin/python3
def weight_average(my_list=[]):
    """function that returns the weighted average of all integers tuple

    Keyword Arguments:
        my_list {list} -- weighted list (default: {[]})

    Returns:
        [float] -- Returns 0 if the list is empty
    """
    if not my_list:
        return 0
    sum = 0
    mul = 0
    for score, weight in my_list:
        mul += score * weight
        sum += weight
    return mul / sum
