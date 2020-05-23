#!/usr/bin/python3
"""[summary]"""


def text_indentation(text):
    """[summary]

    Arguments:
        text {[type]} -- [description]

    Raises:
        TypeError: [description]
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    count = "."
    for c in text:
        if c is " " and count in ".?:":
            continue
        print(c, end="")
        if c in ".:?":
            print("\n")
        count = c
