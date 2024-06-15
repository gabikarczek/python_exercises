# Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.

# The function will have an input of a string, and output a list of integers.

def word_lengths(phrase):
  return list(map(len, phrase.split()))

word_lengths("hello i love my cat")