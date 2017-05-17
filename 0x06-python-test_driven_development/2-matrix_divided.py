#!/usr/bin/python3

'''
matrix divded module


'''


def matrix_divided(matrix, div):
    '''
    test
    '''
    new_list = []
    final_list = []
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None and div is None:
        raise TypeError
    if matrix is None or matrix == []:
        raise TypeError(err_msg)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in matrix[i]:
            if type(j) != int and type(j) != float and type(j) != bool:
                raise TypeError(err_msg)
            result = j / div
            result = float(str(round(result, 2)))
            new_list.append(result)
        final_list.append(new_list)
        new_list = []
    return (final_list)
