#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """Define a rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """height

        Returns:
            [int] -- [Private]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height

        Arguments:
            value {[int]} -- [description]

        Raises:
            TypeError: [height must be an integer]
            ValueError: [height must be >= 0]
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """[summary]

        Returns:
            [int] -- [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width

        Arguments:
            value {[int]} -- [description]

        Raises:
            TypeError: [width must be an integer]
            ValueError: [width must be >= 0]
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """area

        Returns:
            [int] -- [area of rectangle]
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter

        Returns:
            [int] -- [perimeter of rectangle]
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2
