#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_mul = []
    for i in my_list:
        if i % 2 == 0:
            list_mul.append(True)
        else:
            list_mul.append(False)
    return (list_mul)
