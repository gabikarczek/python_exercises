# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    return ''.join(char * 2 for char in s)