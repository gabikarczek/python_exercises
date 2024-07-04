# Write a Python function called multiplication_table that takes an integer n as input and prints the multiplication table from 1 to 10 for that number. For example, if n is 5, the function should print the multiplication table for 5 up to 10x5.

def multiplication_table(number):
  """
  By using the function multiplication_table, you are able to insert a number
    and receive the multiplication table from 1 to 10 for that number. Yay!
  """
  n = int(number)
  for x in range(1,11):
    print(f"{n} x {x} = {n * x}")
    