#!/usr/bin/python3


def add_tuple(tuple_c=(), tuple_d=()):
    if len(tuple_c) < 2:
        if len(tuple_c) == 0:
            tuple_c = 0, 0
        else:
            tuple_c = tuple_c[0], 0
    if len(tuple_d) < 2:
        if len(tuple_d) == 0:
            tuple_d = 0, 0
        else:
            tuple_d = tuple_d[0], 0

    return (tuple_c[0] + tuple_d[0], tuple_c[1] + tuple_d[1])
