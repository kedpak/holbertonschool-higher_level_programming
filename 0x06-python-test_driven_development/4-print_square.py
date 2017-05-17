#!/usr/bin/python3
'''
print square module


'''


def print_square(size):
    '''
    test
    '''
    if type(size) != int and type(size) != bool:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print("")
