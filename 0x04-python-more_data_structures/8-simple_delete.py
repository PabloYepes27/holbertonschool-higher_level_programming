#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """function that deletes a key in a dictionary.

    Arguments:
        a_dictionary {[type]} -- [description]

    Keyword Arguments:
        key {str} -- argument will be always a string (default: {""})

    Returns:
        [dic] -- Dictionary
    """
    if key in a_dictionary.keys():
        a_dictionary.pop(key)
    return a_dictionary
