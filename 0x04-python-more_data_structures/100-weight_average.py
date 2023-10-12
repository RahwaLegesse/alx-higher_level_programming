#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    destination = 0

    for j in my_list:
        number += j[0] * j[1]
        destination += j[1]

    return (number / destination)
