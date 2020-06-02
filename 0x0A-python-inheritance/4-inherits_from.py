#!/usr/bin/python3
"""Write a function that returns True if the object is
 an instance of a class that inherited (directly or indirectly)
  from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """[check if the class of an object is a subclass of a_class
     and if it doesn't is the a_class itself  ]

    Arguments:
        obj {[type]} -- [object of different clases]
        a_class {[type]} -- [random classes]

    Returns:
        [bool] -- [True if the object is an instance
         of a class that inherited; otherwise False]
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
