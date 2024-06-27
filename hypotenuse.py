# Write a function calculate_hypotenuse(a, b) that takes the lengths of the two shorter sides of a right triangle and returns the length of the hypotenuse using the Pythagorean theorem.

import math
def calculate_hypotenuse(a,b):
  return math.sqrt(a**2 + b**2)
  # return math.sqrt(a**2 + b**2)**0.5