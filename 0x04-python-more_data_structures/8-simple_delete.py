#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    switch = True  # need a switch to tell if found matching key
    for i in my_dict:  # will delete more than needed without switch
        if key == i:
            switch = True
            break
        else:
            switch = False
    if switch is True:
        del my_dict[i]
    return (my_dict)
