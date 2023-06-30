#!/usr/bin/python3
"""This module defines a maxtrix_divided function"""

def matrix_divided(matrix, div):
    """Divides all matrix elements by a divisor

    Args:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The divisor.

    Returns:
    List of lists: The new divided matrix.

    Examples:
    >>> # Doctests are located in the seperate file tests/2-matrix_divided.txt
    >>> # Please refer to 'tests/2-matrix_divided.txt' for test cases.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or not all(all(
            isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    # Check for empty matrix or any empty rows in the matrix
    if not matrix or any(not row for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check for rows of different sizes
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return new_matrix
