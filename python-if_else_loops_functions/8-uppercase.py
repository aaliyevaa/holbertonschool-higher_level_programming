#!/usr/bin/python3
def uppercase(st):
    n=''
    for i in st:
        n+=chr(ord(i)-32)
    return n
