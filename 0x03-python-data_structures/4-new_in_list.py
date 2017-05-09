#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list):
        return (my_list[:])
    if idx < 0:
        return (my_list[:])
    temp_list = my_list[:]
    temp_list.pop(idx)
    temp_list[idx:0] = [element]
    return (temp_list)
