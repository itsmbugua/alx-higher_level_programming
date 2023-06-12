#!/usr/bin/python3

def print_matrix_integer(matrix: list = [[]]) -> None:
    """ print a matrix of integers

    Args:
    two dimensional array of integers

    Return:
    None

    """
    for x in matrix:
        for j in range(len(x)):
            if j == len(x) - 1:
                print("{}".format(x[j]))
            else:print("{}".format(x[j]), end=" ")
