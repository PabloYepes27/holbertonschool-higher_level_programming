#!/usr/bin/python3
"""Write a class Student that defines a
 student by: (based on 11-student.py"""


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

    def to_json(self, attrs=None):
        """Public method def to_json(self, attrs=None):
         that retrieves a dictionary representation of
          a Student instance (same as 10-class_to_json.py):

        Returns:
            [dict]: [dictionary representation of
             a Student instance]
        """
        if attrs is None:
            return self.__dict__
        dic = {}
        for elem in attrs:
            if elem in self.__dict__:
                dic[elem] = self.__dict__[elem]
        return dic
