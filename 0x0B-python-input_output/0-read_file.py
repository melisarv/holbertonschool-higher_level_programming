#!/usr/bin/python3
"""Read file function"""


def read_file(filename=""):
    """function that reads a text file and prints"""

    with open(filename, encoding="utf-8") as f:
        for text in f.read():
            print(text, end='')
