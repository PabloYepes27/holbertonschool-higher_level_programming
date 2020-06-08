#!/usr/bin/python3
"""Task 1 : Write the first class Base with a private class attribute
"""


class Base:
    """This class will be the “base” of all other classes in this project.
     The goal of it is to manage id attribute in all your future classes
      and to avoid duplicating the same code (by extension, same bugs)

    nb_objects = private class attribute which is going to increment
                in case the id is None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id ([int]): [increase id to avoid duplicating the same
             code]. Defaults to None.

        To call a class attribute it must be preced the name of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
