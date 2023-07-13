#!/usr/bin/python3
"""This module is a definition of pascal_triangle(n)"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s
    triangle of n
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    # Generate the remaining rows of Pascal's triangle
    for i in range(1, n):
        row = [1]  # First element of each row is always 1

        # Calculate the middle elements of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
