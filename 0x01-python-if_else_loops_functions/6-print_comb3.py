#!/usr/bin/python3
i = 0   # this is the first digit itereator
k = 1   # this is the second digit iterator
m = 9   # this counts number of times of inner loop
j = 2   # this integer sets the count of the inner loop digit itereator
for num in range(0, 10):
    for num2 in range(0, m):
        print('{:d}'.format(i), end="")
        if num < 8:
            print('{:d}, '.format(k), end="")
        else:
            print('{:d}\n'.format(k), end="")
        k = k + 1
    k = j
    j = j + 1
    i = i + 1
    m = m - 1
