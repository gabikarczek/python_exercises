# Write a function rare_n_words(text, n) that takes a string text and an integer n, and returns a list of the n most rare words in the text using the Counter class.

from collections import Counter

def rare_n_words(text, n):
  words = text.split()
  c = Counter(words)
  return (c.most_common(n)[::-1])[:n]