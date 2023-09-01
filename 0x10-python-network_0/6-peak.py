#!/usr/bin/python3
"""Finds Peask."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    first, last = 0, len(list_of_integers) - 1
    while first <= last:
        mid = first + ((last - first) // 2)
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            last = mid - 1
        elif mid < len(list_of_integers) - 1 and list_of_integers[mid] < list_of_integers[mid + 1]:
            first = mid + 1
        else:
            return list_of_integers[mid]
