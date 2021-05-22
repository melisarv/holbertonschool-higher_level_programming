#!/usr/bin/python3
"""
Function text_indentation
text_indentation: prints a text with 2 new lines after charaters ., ?, :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after character ., ?, :
    Args: text is a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    result = text
    for d in "?:.":
        result = (d + "\n\n").join(
                 [x.strip(" ") for x in result.split(d)])

    print(result)
