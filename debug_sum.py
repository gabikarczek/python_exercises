# Debug   function getSumOfDigits that takes positive integer to calculate sum of its digits. Assume that argument is an integer.

def get_sum_of_digits(num):
    str_num = str(abs(num))
    digit_sum = 0
    for digit in str_num:
        digit_sum += int(digit)
    return digit_sum