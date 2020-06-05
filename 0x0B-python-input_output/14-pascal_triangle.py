#!/usr/bin/python3
"""  """


def pascal_triangle(n):
    """[summary]

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    triangle = []
    ls = []
    for row in range(0, n):
        ls = []
        for col in range(0, row + 1):
            if col is 0 or col is row:
                ls.append(1)
            else:
                ls.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        triangle.append(ls)
        print(triangle)
    return triangle
