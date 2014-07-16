import sys
import json
import operator

# Designed to be run from terminal, with this command
# python top_ten.py output.txt

# Load Tweets
def loadTweets(fname):
	tweets = []
	with open(fname, 'rb') as f:
		for line in f:
			tweets.append(json.loads(line))
	return tweets

# Find occurences of terms
def hashtagCount(tweets):
	hashtag_counts = {}

	for tweet in tweets:
		entities = tweet.get("entities")
		if entities:
			hashtags = entities.get("hashtags")
			if hashtags:
				for hashtag in hashtags:
					text = hashtag.get("text")
					if text in hashtag_counts:
						hashtag_counts[text] += 1
					else:
						hashtag_counts[text] = 1

	return hashtag_counts

# Print the top 10 most common hashtags
def topTen(hashtags):
	sorted_tags = sorted(hashtags.iteritems(), key = operator.itemgetter(1), reverse=True)
	for x in range(10):
		tag, score = sorted_tags[x]
		print("%s %s" % (tag, score))

def main():
	tweets = loadTweets(sys.argv[1])
	hashtag_counts = hashtagCount(tweets)
	topTen(hashtag_counts)

if __name__ == '__main__':
	main()
