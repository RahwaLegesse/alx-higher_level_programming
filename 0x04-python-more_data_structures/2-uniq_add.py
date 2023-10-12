#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_uniq = set(my_list)
    number = 0

    for k in list_uniq:
        number += k

    return (number)
