#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """function that computes the square value of all integers of a matrix

    Keyword Arguments:
        matrix {list} -- matrix (default: {[]})

    Returns:
        [list] -- Returns a new matrix
    """
    return list(map((lambda row: (list(map((lambda a: a * a), row)))), matrix))
