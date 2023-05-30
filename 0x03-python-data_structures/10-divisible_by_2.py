#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_divisible = []
    for i in my_list:
        if i % 2 == 0:
            check_divisible.append(True)
        else:
            check_divisible.append(False)
    return check_divisible
