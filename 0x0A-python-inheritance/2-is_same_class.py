#!/usr/bin/python3
""" Write a function that returns True if the object
 is exactly an instance of the specified class;
 otherwise False. """


def is_same_class(obj, a_class):
    """[summary]

    Arguments:
        obj {[type]} -- [object of different clases]
        a_class {[type]} -- [random classes]

    Returns:
        [bool] -- [True if the object
 is exactly an instance of the specified class;
 otherwise False]
    """
    return type(obj) is a_class
