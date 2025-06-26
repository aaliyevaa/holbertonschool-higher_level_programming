#!/usr/bin/python3
"""This module has the solution of Pascal Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of n"""
    if n <=0:
        return []
    main = [[1]]
    for i in range(1,n):
        prev = main[i-1]
        row = [1]
        for j in range(1, len(prev)):
            row.append(prev[j-1] + prev[j])
        row.append(1)
        main.append(row)
    return main
