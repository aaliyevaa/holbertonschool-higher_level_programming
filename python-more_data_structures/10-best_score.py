#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    keys = [key for key in a_dictionary.keys()]
    if len(keys) == 1:
        return None
    maxx = a_dictionary[keys[0]]
    max_key = keys[0]
    for keys in a_dictionary:
        if a_dictionary[keys] > maxx:
            maxx = a_dictionary[keys]
            max_key = keys
    return max_key
