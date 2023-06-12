#!/usr/bin/python3

def multiple_returns(sentence: str) -> tuple:
    """ returns a tuple with the length of a string and its first character

    Args:
    sentence: string value

    Return:
    tuple with the length of string and first character in string

    """
    length = len(sentence)

    if length == 0:
        return (length, None)

    return (lenght, sentence[0])
