#!/usr/bin/python3
"""[Write a function that reads n lines of a text file
 (UTF8) and prints it to stdout:]"""


def read_lines(filename="", nb_lines=0):
    """[read() prit all the text, readline() print each line until
     '\n' is found]

    Args:
        filename (str, optional): [name of the file to
         open and read]. Defaults to "".
        nb_lines (int, optional): [name of the lines to
         print]. Defaults to 0.
    """
    with open(filename, encoding="UTF8") as MyFile:
        if nb_lines > 0:
            for ln in range(nb_lines):
                print(MyFile.readline(), end="")
        else:
            print(MyFile.read(), end="")
