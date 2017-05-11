#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    set2_list = list(set_2)
    set1_list = list(set_1)
    switch = True
    for i in range(0, len(set_1)):
        for j in range(0, len(set_2)):
            if set1_list[i] != set2_list[j]:
                switch = True
            else:
                switch = False
                break
        if switch is True:
            new_list.append(set1_list[i])

    for m in range(0, len(set_2)):
        for k in range(0, len(set_1)):
            if set1_list[k] != set2_list[m]:
                switch = True
            else:
                switch = False
                break
        if switch is True:
            new_list.append(set2_list[m])
    return (set(new_list))
