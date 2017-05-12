#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    for i, j in my_dict.items():
        if key == i:
            j = value
        my_dict[i] = j
    my_dict.update({key: value})
    return (my_dict)
