# Use zip and list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them.

def concatenate(L1, L2, connector):
 return [L1 + connector + L2 for L1, L2 in zip(L1, L2)]

 concatenate(['A','B'],['a','b'],'-')