#!/usr/bin/python3
"""[summary]"""


def add_integer(a, b=98):
    """[summary]

    Arguments:
        a {[type]} -- [description]

    Keyword Arguments:
        b {int} -- [description] (default: {98})

    Raises:
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type] -- [description]
    """
    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
