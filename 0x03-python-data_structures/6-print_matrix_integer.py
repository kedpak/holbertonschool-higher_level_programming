#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row = ' '.join(str(c) for c in row if str(c) not in '[],')
        print(str.format('{:}', row))
