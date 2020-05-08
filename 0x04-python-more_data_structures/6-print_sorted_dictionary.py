#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys.

    Arguments:
        a_dictionary {dic} -- Dictionary
    """
    for i, j in sorted(a_dictionary.items()):
        print("{}: {}".format(i, j))
