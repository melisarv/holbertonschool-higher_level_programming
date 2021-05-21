#!/usr/bin/python3
"""
Function matrix_divided
matrix_divided: divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix when all elements be divided by div
    validation matrix if type list of int/float
    Args: matrix is list of int/float and div is int/float
    """

    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    division = []
    sizelist = 0
    for row in matrix:
        if sizelist > 0 and len(row) != sizelist:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            sizelist = len(row)
        for i in row:
            if isinstance(i, (int, float)) is False:
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")
            division.append(round(i / div, 2))
        new_matrix.append(division)
        division = []
    return new_matrix
