#!/usr/bin/python3
'''


add int module
'''


def add_integer(a, b):
    '''
    test
    '''
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int and type(a) != bool:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != bool:
        raise TypeError('b must be an integer')
    sum = a + b
    return (sum)
