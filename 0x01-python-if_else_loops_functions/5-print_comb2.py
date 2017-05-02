#!/usr/bin/python3
i = 0
k = 0
for num in range(0, 100):
    if num < 99:
        print('{:d}{:d}, '.format(i, k), end="")
    else:
        print('{:d}{:d}\n'.format(i, k), end="")
    k = k + 1
    if k > 9:
        i = i + 1
        k = 0
