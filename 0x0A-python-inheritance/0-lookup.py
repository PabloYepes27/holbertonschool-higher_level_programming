#!/usr/bin/python3
"""[function that returns the list of
    available attributes and methods of an object]
    """


def lookup(obj):
    """
    The dir() function returns all properties and
    methods of the specified object, without the values.

    Arguments:
        obj {[list]} -- [object MyClass of the class object]

    Returns:
        [list] -- [Return a list object]
    """
    return dir(obj)
