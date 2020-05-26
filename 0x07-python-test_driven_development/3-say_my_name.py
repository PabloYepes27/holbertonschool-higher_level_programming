#!/usr/bin/python3
"""[Write a function that prints My name is 
<first name> <last name>]"""


def say_my_name(first_name, last_name=""):
    """[print the full name]

    Arguments:
        first_name {[str]} -- [description]

    Keyword Arguments:
        last_name {str} -- [description] (default: {""})

    Raises:
        TypeError: [first_name must be a string]
        TypeError: [last_name must be a string]
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
 
    if len(first_name) is 0:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
