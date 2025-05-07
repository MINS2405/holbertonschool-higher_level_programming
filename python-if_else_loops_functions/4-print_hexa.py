#!/usr/bin/python3
print("{}".format("".join([str(i) + " = " + hex(i)
                           for i in range(0, 99)])), end="")
