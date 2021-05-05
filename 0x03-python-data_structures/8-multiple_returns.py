#!/usr/bin/python3
def multiple_returns(sentence):

    if len(sentence) == 0:
        tuple_last = 0, "None"
        return (tuple_last)

    tuple_last = len(sentence), sentence[0]

    return (tuple_last)
