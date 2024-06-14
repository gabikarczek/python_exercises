# Move the first letter of each word to the end of it, then add "ay" to the end of the word.

def pig_it(text):
  words = text.split()
  pig_words = []
  for word in words:
    pig_word = word[1:] + word[0] + "ay"
    pig_words.append(pig_word)
  return " ".join(pig_words)

  pig_it('Pig latin is cool')
