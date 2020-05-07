#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function that replaces all occurrences
    of an element by another in a new list.

    Arguments:
        my_list {[list]} -- is the initial list
        search {[int]} -- is the element to replace in the list
        replace {[int]} -- is the new element
    """
    return list(map(lambda i: replace if i == search else i, my_list))
