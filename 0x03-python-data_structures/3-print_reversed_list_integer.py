#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = 0
    for i in reversed(my_list):
        print(str.format('{:d}', i))
