#!/usr/bin/python3
from models.base import Base
"""
Task 2: Write the class Rectangle that inherits from Base
Task 3: Update the class Rectangle by adding validation of
        all setter methods and instantiation (id excluded)
Task 4: Update the class Rectangle by adding the public
        method def area(self): that returns the area value
        of the Rectangle instance.
Task 5: Update the class Rectangle by adding the public method
        def display(self): that prints in stdout the Rectangle
        instance with the character #
Task 6: Update the class Rectangle by overriding the __str__
        method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
"""


class Rectangle(Base):
    """Class Rectangle inherits from Base

    Why private attributes with getter/setter? Why not directly
    public attribute?

    Because we want to protect attributes of our class.
    With a setter, you are able to validate what a developer
    is trying to assign to a variable. So after, in your class
    you can “trust” these attributes.

    Args:
        Base ([type]): [description]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor

        Args:
            width ([type]): [private instance attribute]
            height ([type]): [private instance attribute]
            x (int, optional): [private instance attribute]. Defaults to 0.
            y (int, optional): [private instance attribute]. Defaults to 0.

            id ([type], optional): [ super class with id]. Defaults to None.
            this super call use the logic of the __init__ of the Base class

            use of super():
            https://www.programiz.com/python-programming/methods/built-in/super
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method area

        Returns:
            [int]: [returns the area value of the Rectangle instance]
        """
        return self.__width * self.__height

    def display(self):
        """Public method display the rectangle"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """overriding the __str__ method so that it returns a string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))
