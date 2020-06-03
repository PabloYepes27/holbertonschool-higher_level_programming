#!/usr/bin/python3
"""[Write a class Square that inherits
 from Rectangle (9-rectangle.py):]"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area

        Returns:
            [int] -- [area of rectangle]
        """
        return self.__size * self.__size

    def __str__(self):
        """[str]

        Returns:
            [str] -- [description]
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
