#!/usr/bin/python3
def read_file(filename=""):
    '''function that reads a text file and prints'''

    with open(filename) as f:
        text = f.read()
        print(text, end='')
