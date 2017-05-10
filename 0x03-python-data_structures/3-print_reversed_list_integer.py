#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    my_list.reverse()
    for i in range(0, len(my_list)):
        print(str.format('{:d}', my_list[i]))
