#!/usr/bin/python3

def element_at(my_list, idx: int) -> int:
    """ to get element at specified index
    
    Args:
    my_list: array of integers
    idx: index

    Returns:
    integer at idx if failed return None

    """
    leng = len(my_list) - 1

    if idx < 0 or idx > length:
        return None

    return my_list[idx]
    
