#!/usr/bin/python3
"""Write a function that returns True if the object is an
 instance of, or if the object is an instance of a class
  that inherited from, the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """[subclass of a class]

    Arguments:
        obj {[type]} -- [object of different clases]
        a_class {[type]} -- [random classes]

    Returns:
        [bool] -- [True if the object is an
 instance, or if the object is an instance of a class
  that inherited from; otherwise False]
    """
    return isinstance(obj, a_class)
