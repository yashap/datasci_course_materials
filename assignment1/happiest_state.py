import sys
import csv
import json

# Designed to be run from terminal, with this command
# python tweet_sentiment.py AFINN-111.txt output.txt

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
# def scoreTweets(tweets, scores):
# 	for tweet in tweets:
# 		tweet_score = 0
# 		text = tweet.get("text")
# 		if not tweet.get("text"):
# 			text = ""
# 		words = text.split()
# 		for word in words:
# 			word_score = scores.get(word)
# 			if not word_score:
# 				word_score = 0
# 			tweet_score += word_score
# 		print(tweet_score)

def getTweetLocation(tweet):
	x = tweet.get("place")
	if x:
		x = x.get("bounding_box")
		if x:
			x = x.get("coordinates")
			coords = x[0][0]
			return coords[0], coords[1]

# def storeLocations(tweets):
# 	locations = []

tweets = loadTweets("output.txt")
for tweet in tweets:
	text = tweet.get("text")
	if text:
		loc = getTweetLocation(tweet)
		if loc:
			print loc, text

def main():
	scores = loadSentiment(sys.argv[1])
	tweets = loadTweets(sys.argv[2])
	# scoreTweets(tweets, scores)

if __name__ == '__main__':
	main()
