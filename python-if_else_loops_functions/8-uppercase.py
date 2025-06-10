#!/usr/bin/python3
def uppercase(st):
    for i in st:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i)-32)
        print('{:s}'.format(i), end='')
    print()
