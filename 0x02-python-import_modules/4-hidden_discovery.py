#!/usr/bin/python3
import hidden_4

files = dir(hidden_4)
for i in files:
    if not i.startswith('__'):
        print(i)
