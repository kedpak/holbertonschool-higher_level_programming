#!/usr/bin/python
def max_integer(my_list=[]):
    largest = 0
    for i in my_list:
        if i > largest:
            largest = i
    return (largest)
