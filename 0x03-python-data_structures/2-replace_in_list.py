#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= len(my_list):
        return (my_list)
    if idx < 0:
        return (my_list)
    for i in my_list:
        if i == len(my_list):
            my_list[idx] = element
            return my_list
