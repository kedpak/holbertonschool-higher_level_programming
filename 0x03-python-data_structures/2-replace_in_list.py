#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= len(my_list):
        return (None)
    for i in my_list:
        if i == len(my_list):
            my_list[idx] = element
            return my_list
