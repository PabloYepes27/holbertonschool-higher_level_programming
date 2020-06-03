#!/usr/bin/python3
"""Write a function that writes a string to a text file
 (UTF8) and returns the number of characters written:"""


def write_file(filename="", text=""):
    """[summary]
    “Write” mode will overwrite the file

    Args:
        filename (str, optional): [name of the file to
         open and read]. Defaults to "".
        text (str, optional): [string to add in the text].
         Defaults to "".

    Returns:
        [int]: [number of characters written]
    """
    with open(filename, mode="w", encoding="UTF8") as MyFile:
        return (MyFile.write(text))
