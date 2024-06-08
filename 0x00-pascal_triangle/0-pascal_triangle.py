#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle up to
a given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]: A list of lists of integers representing
        Pascal's Triangle.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    fList = [[1], [1, 1]]
    for i in range(n-2):
        appendList = fList[-1]
        listFromAppendList = [1]
        j = 1
        while j <= (len(appendList) - 1):
            listFromAppendList.append(appendList[j] + appendList[j-1])
            j += 1
        listFromAppendList.append(1)
        fList.append(listFromAppendList)
    return fList
