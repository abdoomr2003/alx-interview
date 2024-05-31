#!/usr/bin/env python3
"""
Module 0-pascal_triangle.py
In this function it will generate pascal triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    :param n: Number of rows in Pascal's Triangle
    :type n: int
    :return: List of lists representing Pascal's Triangle
    :rtype: list
    """
    if n <= 0:
        return []
    triangle = [[1]]  # Start with the first row
    for i in range(1, n):
        # Start each row with '1'
        row = [1]
        # Generate the middle values
        k = i-1
        row.extend([triangle[k][j-1] + triangle[k][j] for j in range(1, i)])
        # End each row with '1'
        row.append(1)
        # Append the generated row to the triangle
        triangle.append(row)

    return triangle
