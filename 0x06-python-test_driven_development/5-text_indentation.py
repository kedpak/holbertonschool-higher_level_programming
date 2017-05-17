#!/usr/bin/python3
'''


text indentation module
'''


def text_indentation(text):
    '''
    test
    '''
    if type(text) != str:
        raise TypeError("text must be a string")
    iter = 0
    while iter < len(text):
        snap = True
        if text[iter] == ' ' and iter == 0:
            while text[iter] is ' ':
                iter += 1
        if text[iter] == '?':
            print(text[iter], end="")
            print("")
            print("")
            iter += 1
            if iter >= len(text):
                break
            if iter <= len(text):
                if text[iter] == ' ':
                    while text[iter] is ' ':
                        iter += 1
            snap = False
        if text[iter] == '.':
            print(text[iter], end="")
            print("")
            print("")
            iter += 1
            if iter >= len(text):
                break
            if text[iter] == ' ':
                while text[iter] is ' ':
                    iter += 1
            snap = False
        if text[iter] == ':':
            print(text[iter], end="")
            print("")
            print("")
            iter += 1
            if iter >= len(text):
                break
            if iter <= len(text) - 1:
                if text[iter] == ' ':
                    while text[iter] is ' ':
                        iter += 1
            snap = False
        if snap is True:
            print(text[iter], end="")
            iter += 1
