#!/usr/bin/python3
"""This module is a definition of text_indentation()"""

def text_indentation(text):
    """
    Searches a string for `.`, `?`, and `:` characters and inserts two newlines
    after each occurance.

    Args:
    text (str): Text to be searched through

    Usage:
    For examples & documentation please refer to ./tests/5-text_indentation.txt
    """
    if not isinstance(text, str): # check if input is of str type
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in punctuations:
            new_text += "\n\n"
    lines = new_text.strip().split("\n")
    new_text = "\n".join(line.strip() for line in lines)

    print(new_text, '\n')
