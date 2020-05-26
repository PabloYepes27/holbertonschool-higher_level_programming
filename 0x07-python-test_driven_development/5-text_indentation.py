#!/usr/bin/python3
"""Write a function that prints a text with 2
 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """indent the text with new lines with delimiters

    Arguments:
        text {[string]} -- [description]

    Raises:
        TypeError: [text must be a string]
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    count = ":"
    for c in text:
        if c is " " and count in ".?:":
            continue
        print(c, end="")
        if c in ".:?":
            print("\n")
        count = c
