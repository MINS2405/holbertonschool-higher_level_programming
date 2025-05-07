#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            # Convert lowercase to uppercase by subtracting 32 from its ASCII value
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
