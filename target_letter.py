# Use filter to return the words from a list of words which start with a target letter.

def filter_words(word_list, letter):
  return list(filter(lambda word: word.startswith(letter), word_list))
  

l = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'cookie', 'tree', 'card', 'heart']
filter_words(l, 'c')