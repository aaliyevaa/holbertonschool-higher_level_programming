#!/usr/bin/python3
def print_last_digit(num):
    if num >= 0:
        return num % 10
    else:
        return num % 10 - 10
