#!/usr/bin/python3


" A class Square that defines a square "


class Square:
    """
    Square class

    Attributes:
        size (int) : Private instance attribute
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
    Public instance method that returns the current square area
    """
    def area(self):
        return self.__size ** 2
