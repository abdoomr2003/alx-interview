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

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
