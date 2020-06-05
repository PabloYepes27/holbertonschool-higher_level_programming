#!/usr/bin/python3
""" Write a function that inserts a line of text to a file, after
 each line containing a specific string (see example): """


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,

    Args:
        filename (str, optional): [description]. Defaults to "".
        search_string (str, optional): [description]. Defaults to "".
        new_string (str, optional): [description]. Defaults to "".
    """
    tmp = ""
    with open(filename, encoding="UTF8") as file:
        for line in file:
            if search_string in line:
                tmp += line[:] + new_string
            else:
                tmp += line[:]
    with open(filename, mode="w", encoding="UTF8") as file:
        file.write(tmp)
