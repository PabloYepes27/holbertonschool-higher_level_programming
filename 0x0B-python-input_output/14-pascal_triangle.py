#!/usr/bin/python3
""" Create a function def pascal_triangle(n): that returns a list
 of lists of integers representing the Pascal’s triangle of n: """


def pascal_triangle(n):
    """Returns an empty list if n <= 0
You can assume n will be always an integer

    Args:
        n ([int]): [height]

    Returns:
        [list]: [triangle]
    """
    if n <= 0:
        return []
    triangle = []
    for row in range(0, n):
        ls = []
        for col in range(0, row + 1):
            if col is 0 or col is row:
                ls.append(1)
            else:
                ls.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        triangle.append(ls)
    return triangle
