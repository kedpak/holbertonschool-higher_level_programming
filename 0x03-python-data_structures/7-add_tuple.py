#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
        my_list = []
        new_t1 = tuple_a + (0, 0)
        new_t2 = tuple_b + (0, 0)
        for i in range(len(tuple_a)):
                my_list.append(new_t1[i] + new_t2[i])
        return tuple(my_list)
