#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as f:
        file_content = f.read()
        print(file_content, end="")
