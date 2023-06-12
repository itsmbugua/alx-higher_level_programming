#!/usr/bin/python3

def replace_in_list(my_list: list, idx: int, element: int) -> list:
    """ to replace element in list

        Args:
            my_list:  array of integers
            idx: index to find item
            element: new item to add in list at index idx

        Returns:
            list of integers

    """
    length = len(my_list) - 1

    if idx < 0 or idx > length:
        return my_list

    del my_list[idx]
    my_list.insert(idx, element)

    return my_list
