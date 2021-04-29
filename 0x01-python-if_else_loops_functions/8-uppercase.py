#!/usr/bin/python3
def uppercase(str):
    for i in str:
        r = ord(i)
        if (r >= 97 and r <= 122):
            r = r - 32
        print("{:c}".format(r), end="")
    print()
