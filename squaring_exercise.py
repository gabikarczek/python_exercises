# Write a function that asks for an integer and prints the square of it. 
# Use a while loop with a try, except, else block to account for incorrect inputs.

def squaring():
  while True:
    try:
      integer = int(input("Provide an integer: "))
    except:
      print("Incorrect data type. Try again: ")
    else:
      print(integer**2)
      break
      
squaring()