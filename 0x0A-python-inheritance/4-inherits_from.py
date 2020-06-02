#!/usr/bin/python3
"""Write a function that returns True if the object is
 an instance of a class that inherited (directly or indirectly)
  from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """[ instance of a class that inherited]

    Arguments:
        obj {[type]} -- [object of different clases]
        a_class {[type]} -- [random classes]

    Returns:
        [bool] -- [True if the object is an instance
         of a class that inherited; otherwise False]
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
