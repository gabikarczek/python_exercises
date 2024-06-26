# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

# If a string contains all repeating characters, it should return an empty string ("").

def first_non_repeating_letter(text):
  letters = ""
  for letter in text.lower():
    if text.count(letter) == 1:
      return letter
  return ""