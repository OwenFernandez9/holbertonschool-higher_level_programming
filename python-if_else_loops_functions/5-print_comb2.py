#!/usr/bin/python3
for a in range(100):
    if a == 99:
        print("{:02d}".format(a), end='\n')
    else:
        print("{:02d}".format(a), end=', ')
