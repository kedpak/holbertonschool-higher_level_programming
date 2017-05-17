#!/usr/bin/python3
'''
name module


'''


def say_my_name(first_name, last_name=""):
    '''
    test
    '''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print('My name is {0} {1}'.format(first_name, last_name))
