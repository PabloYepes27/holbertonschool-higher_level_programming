#!/usr/bin/python3
"""Write a function that returns the JSON
 representation of an object (string):"""


import json


def to_json_string(my_obj):
    """[dumps] Encoding JSON

    Args:
        my_obj ([type]): [object to encoding]

    Returns:
        [string]: [JSON representation of an 0bject]
    """
    return (json.dumps(my_obj))
