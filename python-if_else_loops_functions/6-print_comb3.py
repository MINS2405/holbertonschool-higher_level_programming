#!/usr/bin/python3
print(",".join("{:02d}".format(i) for i in range(100)
               if i % 10 > i // 10), end=", ")
