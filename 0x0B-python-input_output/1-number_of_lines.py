#!/usr/bin/python3
def number_of_lines(filename=""):
    i = 0
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            i += 1
    return (i)
