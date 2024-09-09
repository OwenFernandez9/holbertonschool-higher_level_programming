#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b in a:
            end = ' '
            if b is a[-1]:
                end = ''
            print("{:d}".format(b), end=end)
        print()
