#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new_list = my_list[:]
    for num in my_list:
        if num % 2 > 0:
            new_list[num] = True
        else:
            new_list[num] = False
    return new_list
