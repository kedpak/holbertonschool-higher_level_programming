#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        try:
                iter = 0
                for i in my_list:
                        if iter == x:
                                break
                        print('{:d}'.format(i), end="")
                        iter += 1
                print("")
                return (iter)
        except IndexError:
                for i in my_list:
                        if iter == x:
                                break
                        print('{:d}'.format(i), end="")
                print("")
