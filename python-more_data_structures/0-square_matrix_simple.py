#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        k = []
        for i in row:
            k += [i*i]
        new += [k]
    return new
