#!/usr/bin/python3
"""Write a function that adds 2 integers."""


def add_integer(a, b=98):
    """adds 2 integers.

    Arguments:
        a {[int]} -- [description]

    Keyword Arguments:
        b {int} -- [description] (default: {98})

    Raises:
        TypeError: [a must be an integer]
        TypeError: [b must be an integer]

    Returns:
        [int] -- [addition]
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
