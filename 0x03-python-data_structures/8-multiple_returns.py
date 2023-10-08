#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        return None
    else:
        first = sentence[0]
    return (len(sentence), first)
