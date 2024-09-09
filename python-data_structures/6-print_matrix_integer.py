#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b in a:
            print("{}".format(b), end=' ')
        print()
