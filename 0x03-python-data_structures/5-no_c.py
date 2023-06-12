#!/usr/bin/python3

def no_c(my_string: str) -> str:
    """ to replace all instances of,lowercase and uppercase c

    Args:
    my_string: string to remove all uppercase c

    Returns:
    new string

    """
    return "".jion([x for x in my_string if x != "c" and x != "C"])
