#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix[0] == [] or matrix == None:
        print("")
    for i in range(0, len(matrix)):
        m = 1
        for j in matrix[i]:
            if m < len(matrix):
                print(str.format('{:d}', j), end=" ")
            elif m == len(matrix):
                print(str.format('{:d}', j))
            m += 1
