#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = 'Last digit of {:d} is {:d} and is greater than 5'
str2 = 'Last digit of {:d} is {:d} and is less than 6 and not 0'
str3 = 'Last digit of {:d} is 0 and is 0'
if number > 0:
    if number % 10 > 5:
        print(str1.format(number, abs(number) % 10))
    elif number % 10 < 6 and number % 10 != 0:
        print(str2.format(number, abs(number) % 10))
    elif number % 10 == 0:
        print(str3.format(number))
if number < 0:
    if abs(number) % 10 != 0:
        print(str2.format(number, abs(number) % 10 * -1))
    elif abs(number) % 10 == 0:
        print(str3.format(number))
if number == 0:
    print(str3.format(number))
