#!/usr/bin/python3
import sys
n = len(sys.argv)

if (n == 2):
    print("1 argument:")
elif (n == 1):
    print("0 arguments.")
else:
    print("{:d} arguments:".format(n - 1))

for i in range(n - 1):
    print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
