# This is a  Python script to analyze the word frequency in a text file. The script will read a text file, clean the text by removing
# punctuation and converting all words to lowercase, then count the occurrences of each word. Ultimately, it will print out 
# the list of words along with their frequencies in descending order.

from google.colab import drive
drive.mount('/content/drive')

# first step: importing and reading a text file 

import string
f = open("/content/drive/My Drive/project/chopin.txt", 'r')
text = f.read()
f.close()

# second step: deletion of punctuation

punc = string.punctuation
for p in punc:
  if p in text:
    text = text.replace(p, "")

# thrid step: conversion of the text to lowercase

cleaned = str(text).lower()

# fourth step: counting the occurrences of each word in the text
word_list = cleaned.split()
word_count = {}
for word in word_list:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

# fifth step: reversion of the word order
sorted_dic = sorted(word_count.items(), key = lambda n:n[1], reverse=True)
final_dic = dict(sorted_dic)

# sixth step: storing the words and their occurrences in a dictionary
for key, value in final_dic.items():
 print(f"{key} = {value}")

