#!/usr/bin/python3
"""[summary]"""


def matrix_divided(matrix, div):
    """[summary]

    Arguments:
        matrix {[type]} -- [description]
        div {[type]} -- [description]

    Raises:
        TypeError: [description]
        ZeroDivisionError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type] -- [description]
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"
    if len(matrix) is 0:
        raise TypeError(err1)

    if type(div) not in (int, float):
        raise TypeError(err3)

    if div is 0:
        raise ZeroDivisionError(err4)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(err1)
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(err1)

    if any(len(i) is not len(matrix[0]) for i in matrix):
        raise TypeError(err2)

    return [[round((elem / div), 2) for elem in row] for row in matrix]
