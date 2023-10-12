#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = matrix.copy()

    for k in range(len(matrix)):
        matrix_new[k] = list(map(lambda z: z**2, matrix[k]))

    return (matrix_new)
