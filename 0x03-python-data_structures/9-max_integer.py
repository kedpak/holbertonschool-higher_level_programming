#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    largest = None
    for i in my_list:
        if i > largest:
            largest = i
    return (largest)
