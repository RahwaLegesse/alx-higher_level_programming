#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    key_list = list(a_dictionary.keys())

    for k in key_list:
        number += 1

    return (number)
