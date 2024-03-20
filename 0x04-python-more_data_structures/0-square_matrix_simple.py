#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        array = []
        for j in range(len(matrix[i])):
            array.append(matrix[i][j] ** 2)
        new_matrix.append(array)
    return new_matrix
