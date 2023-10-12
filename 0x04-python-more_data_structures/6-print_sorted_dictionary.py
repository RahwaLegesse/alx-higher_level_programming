#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = list(a_dictionary.keys())
    order.sort()
    for k in order:
        print("{}: {}".format(k, a_dictionary.get(k)))
