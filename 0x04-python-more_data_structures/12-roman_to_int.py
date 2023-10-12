#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    maxl = max(list_num)

    for num in list_num:
        if maxl > num:
            sub += num

    return (maxl - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    romn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listk = list(romn.keys())

    number = 0
    lastr = 0
    listm = [0]

    for ch in roman_string:
        for r_num in listk:
            if r_num == ch:
                if romn.get(ch) <= lastr:
                    number += to_subtract(listm)
                    listm = [romn.get(ch)]
                else:
                    listm.append(romn.get(ch))

                lastr = romn.get(ch)

    number += to_subtract(listm)

    return (number)
