#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        num = 0
        for k, v in a_dictionary.items():
            if num < v:
                num = v
                key = k
        return (key)
    else:
        return (None)
