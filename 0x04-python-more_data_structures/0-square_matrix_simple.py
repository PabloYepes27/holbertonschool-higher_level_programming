#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """function that computes the square value of all integers of a matrix.

    Keyword Arguments:
        matrix {list} -- is a 2 dimensional array (default: {[]})

    Returns:
        [list] -- Returns a new matrix
    """
    return [[elem ** 2 for elem in row] for row in matrix]
