#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return (0)
    resul1 = 0
    resul2 = 0
    for i in my_list:
        resul1 += i[0] * i[1]
        resul2 += i[1]
    return (resul1 / resul2)
