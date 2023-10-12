#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_new = list(map(lambda z: replace if z == search else z, my_list))
    return (list_new)
