#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    j = 0
    for i in my_list:
        if i % 2 == 0:
            i = True
            new_list.append(i)
        else:
            i = False
            new_list.append(i)
        j += 1
    return (new_list)
