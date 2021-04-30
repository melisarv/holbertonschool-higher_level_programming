#!/usr/bin/python3
import sys

resul = 0

for i, arg in enumerate(sys.argv):
    if (i > 0):
        resul += int(arg)

print(resul)
