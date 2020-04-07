#!/usr/bin/env python
# from bnplib import *
from bnplib import ham, spam, get_message, say_hello, square_root

def main():
    """
    Program entry point

    :return: None
    """
    ham(3, 'a')

    m = get_message()
    print(m)

    say_hello()

    print(square_root(2), square_root(100), square_root(20932093))

    spam(1, 2, 3)

    try: # if no exceptions...
        result = spam('a', 'b', 'c')
    except TypeError as err:
        print(err)
    else:
        print(result)

    spam(3, [1, 2, 3], 5)


if __name__ == '__main__':  # if I'm the "main" script
    main()

