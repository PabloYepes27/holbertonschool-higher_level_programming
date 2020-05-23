#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [[None], [1, 2]]
print(matrix_divided(matrix, 3))
print(matrix)

matrix = [[2, 3], [1, 2]]
print(matrix_divided(matrix, float('inf')))
print(matrix)