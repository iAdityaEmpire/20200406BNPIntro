#!/usr/bin/env python
"""
Outstanding examples of functions for the best students EVER.
"""
import typing as T

Numeric = T.Union[int, float]

def get_message():
    """
    Return a greeting.

    Blah blah blahdeby blah

    :return: None
    """
    return "Hello, world"


def say_hello():
    """
    Greet people nicely

    :return: None
    """
    message = get_message()
    print(message)


#  in the function: parameters
#  calling the function: arguments


def square_root(n: Numeric) -> float:
    """
    Return square root of any number

    :param n: Number to get root of
    :return: Square root, as a float
    """
    return n ** .5



# r = square_root()

def spam(a, b, c) -> T.Any:
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    print(a, b, c)
    return 42


def ham(a: Numeric, b: str) -> T.Iterable:
    print(a, b)
    return [a, b]

if __name__ == '__main__':  # if run as primary (main) script with python THIS_SCRIPT.py
    print("WOMBATS!")
    print(ham(5, 'abc'))

