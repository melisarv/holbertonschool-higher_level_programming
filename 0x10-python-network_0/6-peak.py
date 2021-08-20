#!/usr/bin/python3
"""function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    loi = list_of_integers
    total = len(loi)
    if total == 0:
        return None
    elif total == 1:
        return loi[0]
    elif total == 2:
        return max(loi)

    mid = total // 2
    peak = loi[mid]
    if peak > loi[mid + 1] and peak > loi[mid - 1]:
        return peak
    elif peak < loi[mid - 1]:
        return find_peak(loi[:mid])
    return find_peak(loi[mid + 1:])
