#!/usr/bin/env python
"""
Outstanding examples of functions for the best students EVER.
"""
import bnplib

def main():
    """
    Program entry point

    :return: None
    """
    bnplib.ham(3, 'a')

    m = bnplib.get_message()
    print(m)

    bnplib.say_hello()

    print(bnplib.square_root(2), bnplib.square_root(100), bnplib.square_root(20932093))

    bnplib.spam(1, 2, 3)
    try:
        bnplib.spam('a', 'b', 'c')
    except TypeError as err:
        print(err)

    bnplib.spam(3, [1, 2, 3], 5)



main()

