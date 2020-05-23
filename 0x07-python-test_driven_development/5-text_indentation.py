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

    for delim in ":.?":
        text = str(delim + "\n\n").join(s.strip() for s in text.split(delim))
    print(text, end="")