#!/usr/bin/python3
"""
Module 2-matrix_divided.py

"""


def matrix_divided(matrix, div):
    """
    devide every item in all matrix by div
    Return: new matrix
    """
    if not isinstance(matrix, list) or not \
        all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

        new_row = [round(i / div, 2) for i in row]
        new_matrix.append(new_row)
    return new_matrix
