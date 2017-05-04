#!/usr/bin/python3
from sys import argv
a = 0
for i in argv:
    if argv.index(i) > 0:
        a = a + int(i)
print('{:d}'.format(a))


def main():
    pass

if __name__ == "__main__":
    main()
