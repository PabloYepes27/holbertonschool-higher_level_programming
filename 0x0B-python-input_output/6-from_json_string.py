#!/usr/bin/python3
"""[Write a function that returns an
 object (Python data structure) represented
  by a JSON string:]"""


import json


def from_json_string(my_str):
    """[loads] Decoding JSON

    Args:
        my_str ([str]): [JSON string]

    Returns:
        [type]: [object]
    """
    return(json.loads(my_str))
