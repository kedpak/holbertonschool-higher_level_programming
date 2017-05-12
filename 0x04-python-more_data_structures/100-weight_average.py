#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return (0)
    score = 0
    weight = 0
    for i, j in my_list:
        score = score + i * j
        weight = weight + j
    average = score/weight
    return (average)
