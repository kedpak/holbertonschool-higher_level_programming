#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for i, j in my_dict.items():
        j = j * 2
        new_dict[i] = j
    return (new_dict)
