#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list):
        return (None)
    if idx < 0:
        return (None)
    for i in my_list:
        if i == len(my_list):
            return my_list[idx]
