#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """function that deletes keys with a specific value in a dictionary.

    Arguments:
        a_dictionary {dic} -- Dictionary
        value {str} -- value to check in dictionary

    Returns:
        [type] -- The directory modified or the same if the value doesn't exist
    """
    tmp_dictionary = a_dictionary.copy()
    for key, v in tmp_dictionary.items():
        if v == value:
            a_dictionary.pop(key)
    return a_dictionary
