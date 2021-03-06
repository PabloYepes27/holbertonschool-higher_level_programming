#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """Define a rectangle

    Raises:
        TypeError: [width must be an integer]
        ValueError: [width must be >= 0]
        TypeError: [height must be an integer]
        ValueError: [height must be >= 0]

    Returns:
        [int] -- [description]
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constructor

        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """str

        Returns:
            [str] -- [description]
        """
        string = ""
        if self.__width is 0 or self.__height is 0:
            return string
        for i in range(0, self.__height - 1):
            string += ("#" * self.__width) + "\n"
        string += "#" * self.__width
        return string

    def __repr__(self):
        """representation

        Returns:
            [type] -- [description]
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """del"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
