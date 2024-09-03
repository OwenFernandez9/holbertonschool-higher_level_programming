#!/usr/bin/python3
for a in range(100):
    if a == 99:
        print("{0}".format(a), end='\n')
    elif a >= 0 and a <= 9:
        print("0{0}".format(a), end=', ')
    else:
        print("{0}".format(a), end=', ')
