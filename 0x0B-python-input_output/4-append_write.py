#!/usr/bin/python3
"""  Write a function that appends a string
 at the end of a text file (UTF8) and returns
  the number of characters added:  """


def append_write(filename="", text=""):
    """ “Append” mode will add data to the
     end of the file. Pass mode='a' to the
      open() function.

    Args:
        filename (str, optional): [name of the file to
         open and read]. Defaults to "".
        text (str, optional): [string to append in the text].
         Defaults to "".

    Returns:
        [int]: [number of characters added]
    """
    with open(filename, mode="a", encoding="UTF8") as MyFile:
        return (MyFile.write(text))
