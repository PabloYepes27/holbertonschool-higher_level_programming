#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(elem) for elem in row))
'''if not matrix:
        print()
    else:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if j == len(matrix[j]) - 1:
                    print("{:d}".format(matrix[i][j]), end="")
                else:
                    print("{:d} ".format(matrix[i][j]), end="")
            print()'''
