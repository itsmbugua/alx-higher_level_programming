#!/usr/bin/python3

def print_reversed_list_integer(my_list: list = []) ->None:
    """ to print all integers in reverse

    Args:
    my_lists: list of integers

    Return:
    None

    """
    if my_list:
        for x in reversed(my_list):
            print("[:d]".format(x))
