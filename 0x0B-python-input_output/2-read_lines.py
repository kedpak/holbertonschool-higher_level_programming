#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    iter = 0
    i = 0
    with open(filename, 'r') as f:
        for j, line in enumerate(f):
            i += 1
    with open(filename, 'r') as f:
        if nb_lines <= 0 or nb_lines >= i:
            file_content = f.read()
            print(file_content, end="")
        elif nb_lines is None:
            file_content = f.read()
            print(file_content, end="")
        else:
            file_lines = f.readlines()
            for m in range(0, nb_lines):
                print(file_lines[iter], end="")
                iter += 1
