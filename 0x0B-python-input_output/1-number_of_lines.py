#!/usr/bin/python3
"""[Write a function that returns the
 number of lines of a text file:]"""


def number_of_lines(filename=""):
    """[count the number of lines of a text]

    Args:
        filename (str, optional): [name of the file to
         open and read]. Defaults to "".
    """
    count = 0
    with open(filename, encoding="UTF8") as MyFile:
        for line in MyFile:
            count += 1
    return(count)
