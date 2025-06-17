#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    summ = 0
    div_sum = 0
    for tuples in my_list:
        summ += tuples[0] * tuples[1]
        div_sum += tuples[1]
    return summ / div_sum
