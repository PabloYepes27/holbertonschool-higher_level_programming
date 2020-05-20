#!/usr/bin/python3


" A class Square that defines a square "


class Square:
    """
    Square class

    Attributes:
        size (int) : Private instance attribute
        position (tuple) : Private instance attribute,
        the first argument is the name of the spaces to the left,
        the second argument is the new lines before print
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    """
    Public instance method that returns the current square area

    Returns: Area of the aquare
    """
    def area(self):
        return self.__size ** 2
    """
    Public instance method that prints in the square with the character #
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
