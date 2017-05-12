#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return (None)
    temp = 0
    for i, j in my_dict.items():
        if j > temp:
            temp = j
    return (temp)
