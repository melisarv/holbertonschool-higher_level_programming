#!/usr/bin/python3
"""Write file function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file and returns
    the number of characters written"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
