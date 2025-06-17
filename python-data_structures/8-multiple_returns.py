#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        l = None
    else:
        l = len(sentence)
    return (l, sentence[0])
