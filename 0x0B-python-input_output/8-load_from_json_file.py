#!/usr/bin/python3
"""Write a function that creates an
 Object from a “JSON file”:"""


import json


def load_from_json_file(filename):
    """
    json.dumps() method can convert a Python object into a JSON string.
    json.dump() method can be used for writing to JSON file.

    json.loads() expects to get its text from a string object
    json.load() expects to get the text from a file-like object

    Args:
        filename ([type]): [description]
    """
    with open(filename, encoding="utf-8") as My_File:
        return json.load(My_File)
