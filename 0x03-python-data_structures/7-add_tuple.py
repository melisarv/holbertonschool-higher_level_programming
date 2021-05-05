#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    while len(tuple_a) < 2:
        tuple_a += (0,)
    while len(tuple_b) < 2:
        tuple_b += (0,)

    first_tuple = tuple_a, tuple_b

    sum1 = sum([par[0] for par in first_tuple])
    sum2 = sum([par[1] for par in first_tuple])

    last_tuple = sum1, sum2
    return (last_tuple)
