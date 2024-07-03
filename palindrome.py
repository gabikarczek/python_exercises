# Write a Python function called is_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise.

def is_palindrome(word):
  if not isinstance(word, str):
    return False
  if word == word[::-1]:
    return True
  else:
    return False