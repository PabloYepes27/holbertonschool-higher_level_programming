#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """
        Student to JSON
    """
    def __init__(self, first_name, last_name, age):
        """constructor

        Args:
            first_name ([type]): [description]
            last_name ([type]): [description]
            age ([type]): [description]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method def to_json(self): that
         retrieves a dictionary representation of
          a Student instance

        Returns:
            [dict]: [dictionary representation of
             a Student instance]
        """
        return self.__dict__
