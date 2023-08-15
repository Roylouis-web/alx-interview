#!/usr/bin/python3
"""
    Module a function named rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
        a function that returns a 2d list with its values
        shifted 90 degrees clockwise
    """

    result = []
    le = len(matrix)

    for i in range(len(matrix)):
        temp = []
        k = 1
        for j in range(len(matrix)):
            temp.append(matrix[le - k][i])
            k += 1
        result.append(temp)

    for i in range(len(result)):
        for j in range(len(result)):
            matrix[i][j] = result[i][j]
