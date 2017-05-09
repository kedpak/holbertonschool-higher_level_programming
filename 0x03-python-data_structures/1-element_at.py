#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list):
        return (None)
    for i in my_list:
        if i == my_list[idx]:
            return my_list[idx]
