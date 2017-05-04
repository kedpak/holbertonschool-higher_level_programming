#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print('0 argument.')
if len(argv) == 2:
    print('1 argument:\n1: {0}'.format(argv[1]))
if len(argv) > 2:
    print('{:d} arguments:'.format(len(argv) - 1))
    for i in argv:
        if argv.index(i) > 0:
            print('{0}: {1}'.format(argv.index(i), i))


def main():
    pass

if __name__ == "__main__":
    main()
