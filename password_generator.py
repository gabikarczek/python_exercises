# Write a function that generates a random password of a given length. 
# The password should contain uppercase and lowercase letters, digits, and special characters.

import random
import string

def generate_password(length):
  uppercase = string.ascii_uppercase
  lowercase = string.ascii_lowercase
  digits = string.digits
  punctuation = string.punctuation
  characters = list(uppercase + lowercase + digits + punctuation)
  return''.join(random.choices(population=characters,k=length))

  print(generate_password(25))