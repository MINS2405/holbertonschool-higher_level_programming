#!/usr/bin/python3
for a in range(10):
    for u in range(a + 1, 10):
        if a == 8 and u == 9:
            print("{:d}{:d}".format(a, u))
        else:
            print("{:d}{:d}, ".format(a, u), end="")
