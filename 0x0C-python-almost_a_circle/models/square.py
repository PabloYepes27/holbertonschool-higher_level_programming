#!/usr/bin/python3
from models.rectangle import Rectangle
"""
Task 10: Write the class Square that inherits from Rectangle
Task 11: Update the class Square by adding the public getter and setter size
Task 12: Update the class Square by adding the public method def update
         (self, *args, **kwargs) that assigns attributes
Task 14: Update the class Square by adding the public method def
         to_dictionary(self): that returns the dictionary representation of a
         Square
"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ method so that it returns a new string"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter

        Returns:
            [int]: [private instance attribute]
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter should assign width and height with the same value

        The setter should have the same value validation as the
        Rectangle for width and height

        __setattr__(self, name, value)
        super().__setattr__(name, value)

        (name) - The name of the attribute.
        (value) - The value we want to assign to the attribute.
        """
        super().__setattr__('width', value)
        super().__setattr__('heigth', value)

    def update(self, *args, **kwargs):
        """method that assigns attributes"""
        attr = ['id', 'size', 'x', 'y']
        if args is None or not args:
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            for n in range(len(args)):
                setattr(self, attr[n], args[n])

    def to_dictionary(self):
        """method that returns the dictionary representation
        of a Square"""
        return dict(id=self.id, x=self.x, y=self.y,
                    size=self.size)
