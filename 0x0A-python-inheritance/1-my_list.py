#!/usr/bin/python3
class MyList(list):     # setting up class with list inheritance
    def __init__(self):  #  init does not have any special functions
        pass

    def print_sorted(self):    #  printing a sorted list
        print(sorted(self))
