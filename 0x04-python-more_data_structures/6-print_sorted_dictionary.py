#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for i, j in sorted(my_dict.items()):
        print("{0}: {1}".format(i, j))
