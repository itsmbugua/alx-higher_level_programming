#!/usr/bin/python3

""" module to get sum of two integers
"""


def add_integer(a, b=98) -> int:
    """ get sum of integers
        Args:
            a: value a can be an integer or float
            b: value be can be an integer or float
        Return:
            integer representing the sum of a and b
    """

    # check if a is not an int or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # check if b is not an int or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # type cast a
    if isinstance(a, float):
        a = int(a)
    # type cast b
    if isinstance(b, float):
        b = int(b)

    return a + b
