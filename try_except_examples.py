#!/usr/bin/env python

foo = ['a', 'b', 'c']

try:
    print(foo[10])
except IndexError as err:
    print(err)

try:
    with open('DATA/moose_muffins.txt') as mm_in:
        pass
except FileNotFoundError as err:
    print(err)

print("All finished")
