#!/usr/bin/python3
"""[]"""


def read_lines(filename="", nb_lines=0):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        nb_lines (int, optional): [description]. Defaults to 0.
    """
    with open(filename, encoding="UTF8") as MyFile:
        if nb_lines > 0:
            for ln in range(nb_lines):
                print(MyFile.readline(), end="")
        else:
            print(MyFile.read(), end="")
