#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ function that replaces or adds key/value in a dictionary.

    Arguments:
        a_dictionary {dic} -- Dictionary
        key {string} -- argument will be always a string
        value {any} -- argument will be any type

    Returns:
        [dic] -- Dictionary modified
    """
    a_dictionary[key] = value
    return a_dictionary
