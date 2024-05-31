#!/usr/bin/env python3
def pascal_triangle(n):
    try:
        if n <= 0:
            return []
        else:
            lists = []
            for i in range(n):
                row = []
                for j in range(i + 1):
                    row.append(fact(i) // (fact(j) * fact(i - j)))
                lists.append(row)
            return lists
    except Exception:
        return []
