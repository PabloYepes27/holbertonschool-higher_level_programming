#!/usr/bin/python3


" A class Square that defines a square "


class Square:
    """
    Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """[summary]

        Keyword Arguments:
            size {int} -- [description] (default: {0})
            position {tuple} -- [the first argument is the name of the
            spaces to the left, the second argument is the new lines
            before print] (default: {(0, 0)})
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """[summary]

        Returns:
            [int] -- [size]
        """
        return self.__size

    @size.setter
    def size(self, value):
        """[summary]

        Arguments:
            value {[int]} -- [size]

        Raises:
            TypeError: [size must be an integer]
            ValueError: [size must be >= 0]
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """[summary]

        Returns:
            [tuple] -- [description]
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) is 2 and
                value[0] >= 0 and value[1] >= 0 and
                isinstance(value[0], int) and isinstance(value[1], int)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
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
        """[summary]
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
