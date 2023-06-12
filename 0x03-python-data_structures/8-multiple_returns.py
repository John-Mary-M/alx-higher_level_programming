#!/usr/bin/python3
def multiple_returns(sentence):
    """
    returns tuple with the length of a string and its first character
    Args:
    sentence (_str_): _description_ sentence to work with
    """
    if sentence == '':
        return (len(sentence), None)
    x = sentence
    return (len(x), x[0])
