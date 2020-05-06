#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new_list = my_list[:]
    for num in range(0, len(my_list)):
        if my_list[num] % 2 > 0:
            new_list[num] = False
        else:
            new_list[num] = True
    return new_list
