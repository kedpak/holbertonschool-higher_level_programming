#!/usr/bin/python3
import hidden_4
import sys

for i in dir(hidden_4):
    if i[:2] != "__":
        print('{0}'.format(i))


def main():
    pass

if __name__ == "__main__":
    main()
