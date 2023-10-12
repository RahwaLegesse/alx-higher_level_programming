#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dirn = a_dictionary.copy()
    listk = list(dirn.keys())

    for k in listk:
        dirn[k] *= 2

    return (dirn)
