#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{0}".format(i))
    else:
        print("{:02}".format(i), end=', ')
