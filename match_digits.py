# Write a Python program that uses regular expressions to find and print all the digits in a given string. Prompt the user to enter a string, then print all the digits found in the input string.

import re

text = input("enter a string: ")

match = re.findall(r'\d', text)

if match:
  print(f"all digits can be found here: {match}")
else:
  print("no match found!")
