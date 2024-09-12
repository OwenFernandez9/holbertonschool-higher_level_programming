#!/usr/bin/python3
"""
A function that divide 2 integers.
"""


def matrix_divided(matrix, div):
    """
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be \
a matrix (list of lists) of integers/floats")
    len_first_row = len(matrix[0])
    new_matrix = list(matrix)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for a in new_matrix:
        if len(a) != len_first_row:
            raise TypeError(
                "Each row of the matrix must have the same size")
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
    new_matrix = [[round(x / div, 2) for x in a] for a in new_matrix]
    return new_matrix
