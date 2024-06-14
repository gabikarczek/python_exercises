# Making the process of marking parts of speech in my syntax assignment more bearable! :)


import nltk 
nltk.download("all")

text = "A young boy from Idaho said that his very wonderful mother had baked him a tasty cheesecake for Labor Day. It had raisins from distant shores of Columbia. He claims that these raisins are very tasty and juicy. We know they are not expensive but very hard to purchase on the open market. The boy has been interrogated by the Police about his claims being true. They have found that there is evidence that the raisins were from Africa. The police believe that the young man has been making things up. They think the cake itself had African raisins and it was purchased in an secret exotic store that has been catering to the very rich for many centuries."

import string

punctuation = string.punctuation

text = text.translate(str.maketrans('', '', string.punctuation))

tokenized = nltk.word_tokenize(text)

tuples = []

pos_tagged = nltk.pos_tag(tokenized)
for item in pos_tagged:
  tuples.append(item)

print(tuples)