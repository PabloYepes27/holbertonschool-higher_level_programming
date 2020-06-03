#!/usr/bin/python3
"""[Write a function that reads a text file
 (UTF8) and prints it to stdout]"""


def read_file(filename=""):
    """[with] statement ensures that the file is closed
     when the block inside the with statement is exited.

    Args:
        filename (str, optional): [name of the file to
         open and read]. Defaults to "".
    """
    with open(filename, mode="r", encoding="UTF8") as MyFile:
        for line in MyFile:
            print(line, end="")
