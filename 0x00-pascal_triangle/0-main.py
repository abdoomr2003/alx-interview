#!/usr/bin/python3
"""
Module 0-main

This module imports the pascal_triangle function and uses it to generate and
print Pascal's Triangle.
"""

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


def print_triangle(triangle):
    """
    Print Pascal's Triangle.

    Args:
        triangle (List[List[int]]): Pascal's Triangle represented as
        a list of lists of integers.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    usrInput= int(input("give me number of rows: "))
    print_triangle(pascal_triangle(usrInput))
