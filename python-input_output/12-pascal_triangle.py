#!/usr/bin/python3
'''
This module returns a list of lists of integers
 representing the Pascal’s triangle
'''


def pascal_triangle(n):
    '''
    Returns a list of lists representing Pascal's triangle of size n

    Args: n (int): Size of the Pascal's triangle

    Returns: list: List of lists representing Pascal's triangle

    '''
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)

        row.append(1)
        triangle.append(row)

    return triangle
