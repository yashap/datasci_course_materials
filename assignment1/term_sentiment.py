import sys
import csv
import json

# Designed to be run from terminal, with this command
# python term_sentiment.py AFINN-111.txt output.txt

# Load AFINN file
def loadSentiment(fname):
	scores = {}
	with open(fname, 'rb') as f:
		content = csv.reader(f, delimiter="\t")
		for line in content:
			scores[line[0]] = int(line[1])
	return scores

# Load Tweets
def loadTweets(fname):
	tweets = []
	with open(fname, 'rb') as f:
		for line in f:
			tweets.append(json.loads(line))
	return tweets

# Print tweet scores
def newTermScore(tweets, scores):
	new_terms = {}

	for tweet in tweets:
		tweet_score = 0
		text = tweet.get("text")
		if not tweet.get("text"):
			text = ""
		words = text.split()

		for word in words:
			word_score = scores.get(word)
			if not word_score:
				word_score = 0
				if word not in new_terms:
					new_terms[word] = 0
			tweet_score += word_score

		for word in words:
			if word not in scores:
				new_terms[word] += tweet_score

	return new_terms

# Print dictionary in "key value" format
def printDict(my_dict):
	for item in my_dict:
		print("%s %s" % (item, my_dict[item]))

def main():
	scores = loadSentiment(sys.argv[1])
	tweets = loadTweets(sys.argv[2])
	new_terms = newTermScore(tweets, scores)
	printDict(new_terms)

if __name__ == '__main__':
	main()
