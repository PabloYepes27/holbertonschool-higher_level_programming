#!/usr/bin/python3
"""[Write a function that multiplies 2 matrices:]"""


def matrix_mul(m_a, m_b):
    """[Multiply to matrix]

    Arguments:
        m_a {[list of list]} -- [description]
        m_b {[list of list]} -- [description]

    Raises:
        TypeError: [m_a must be a list]
        TypeError: [m_b must be a list]
        TypeError: [m_a must be a list of lists]
        TypeError: [m_a can't be empty]
        TypeError: [m_a should contain only integers or floats]
        TypeError: [m_b must be a list of lists]
        ValueError: [m_b can't be empty]
        ValueError: [each row of m_a must be of the same size]
        TypeError: [each row of m_b must be of the same size]
        TypeError: [m_b should contain only integers or floats]
        ValueError: [m_a and m_b can't be multiplied]
    """
    m_c = []
    m_temp = []
    if type(m_a) is not (list):
        raise TypeError("m_a must be a list")

    if type(m_b) is not (list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not (list):
            raise TypeError("m_a must be a list of lists")
        elif len(row) == 0:
            raise ValueError("m_a can't be empty")
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if type(row) is not (list):
            raise TypeError("m_b must be a list of lists")
        elif len(row) == 0:
            raise ValueError("m_b can't be empty")
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a) is 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) is 0:
        raise ValueError("m_b can't be empty")

    if len(set([len(row) for row in m_a])) is not 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set([len(row) for row in m_b])) is not 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            m_temp.append(sum)
        m_c.append(m_temp)
        m_temp = []

    return(m_c)
