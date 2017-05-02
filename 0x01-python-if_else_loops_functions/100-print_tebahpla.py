#!/usr/bin/python3
for letter in reversed(range(97, 123)):
    if letter % 2 == 1:
        letter = letter - 32
    print('{0}'.format(chr(letter)), end="")
