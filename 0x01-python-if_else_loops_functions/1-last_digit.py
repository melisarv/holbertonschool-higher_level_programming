#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string = "Last digit of"

if (number < 0):
    last = number % -10
elif (number >= 0):
    last = number % 10

if (last < 6 and last != 0):
    string2 = "and is less than 6 and not 0"
elif (last == 0):
    string2 = "and is 0"
elif (last > 5):
    string2 = "and is greater than 5"

print("{} {} is {} {}".format(string, number, last, string2))
