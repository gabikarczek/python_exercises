import json
import re

json_tweets = [
 {"tweet_id": 1, "text": "I love the new features in this app!"},
 {"tweet_id": 2, "text": "This update is terrible."},
 {"tweet_id": 3, "text": "Decent app, could be better."}
]

with open('tweets.json', 'w') as file:
    json.dump(json_tweets, file, indent=4)

with open('tweets.json', 'r') as file:
    data = json.load(file)

positive_comments = []
negative_comments = []
neutral_comments = []

positive_patterns = [
    r"i?\s(lov(?:es|ed|e))\s?",
    r"(it's|its)?\s(amazing|wonderful|practical|great|good|exquisite)\s?",
    r"(the|this)?\s(update|app)\sis\s(amazing|wonderful|practical|great|good|exquisite)\s?"
]

negative_patterns = [
    r"(the|this)?\s(update|app)\sis\s(terrible|bad|horrendous|not working|poor|unsatisfactory)\s?",
    r"i?\s(hat(?:es|ed|e))\s?",
    r"(it's|its)?\s(terrible|bad|horrendous|not working|poor|unsatisfactory)\s?"
]

neutral_patterns = [ 
    r"(a|an)?\s(decent|okay|acceptable|adequate|sufficient)\s(update|app)?",
    r"(could|should|might|may|can)\sbe\sbetter",
    r"(it's|its)?\s(decent|okay|acceptable|adequate|sufficient)\s?"
]

for tweet in data:
  tweet_content = tweet["text"]
  for positive_pattern in positive_patterns:
    if re.search(positive_pattern, tweet_content, re.IGNORECASE):
      positive_comments.append(tweet_content)
      tweet['sentiment'] = "positive"
      break
  for negative_pattern in negative_patterns:
    if re.search(negative_pattern, tweet_content, re.IGNORECASE):
      negative_comments.append(tweet_content)
      tweet['sentiment'] = "negative"
      break
  for neutral_pattern in neutral_patterns:
    if re.search(neutral_pattern, tweet_content, re.IGNORECASE):
      neutral_comments.append(tweet_content)
      tweet['sentiment'] = "neutral"
      break

with open('tweets_with_sentiment.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('tweets_with_sentiment.json', 'r') as file:
    tweets_with_sentiment = json.load(file)
print(tweets_with_sentiment)
