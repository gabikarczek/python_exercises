# Write a function to display an indexed value from a given list. Handle possible errors.

def indexed_value(number, user_list):
  try:
    for el in user_list:
      return user_list[number]
  except TypeError:
    print("Incorrect data type. Enter an integer (index number) first, then a list.")
  except IndexError:
    print("Index out of range.")

indexed_value(2, ["hello", "world", "welcome"]) # this should return 'welcome'
indexed_value(7, ["hello", "world", "welcome"]) # this should return 'Index out of range'
indexed_value(2, 4) # this should return 'Incorrect data type. Enter an integer (index number) first, then a list.'