# Write a Python function called sum_of_digits that takes an integer as input and returns the sum of its digits. For example, if the input is 123, the function should return 6 (since 1 + 2 + 3 = 6)

def sum_of_digits(num):
  """
  By using the function sum_of_digits, you are able to insert a random integer
            and receive back the sum of its digits. Fun, isn't it?
  """
  str_num = str(abs(num))
  digit_sum = 0
  for digit in str_num:
    digit_sum += int(digit)
  return digit_sum