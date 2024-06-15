# The function merges two lists: animals and count, and returns a final list of each animal and its corresponding count.

def merge_list(animals, count):
  final_list = list(zip(animals, count))
  formatted_list = [f"animal: {animals}, count: {count}" for animals, count in final_list]
  return formatted_list

# Attempt

animals = ["cats", "cows", "dogs"]
count = [27, 20, 42]

print(merge_list(animals,count))