import sys
import json

# Designed to be run from terminal, with this command
# python frequency.py output.txt

# Load Tweets
def loadTweets(fname):
	tweets = []
	with open(fname, 'rb') as f:
		for line in f:
			tweets.append(json.loads(line))
	return tweets

# Find occurences of terms
def termOccurences(tweets):
	term_counts = {}
	all_terms = 0

	for tweet in tweets:
		text = tweet.get("text")

		if text:
			words = text.split()

			for word in words:
				word_count = term_counts.get(word)
				if word_count:
					term_counts[word] += 1
				else:
					term_counts[word] = 1
				all_terms += 1

	return term_counts, all_terms

# Find term frequency
def termFreq(term_counts, all_terms):
	frequencies = {}
	all_terms = all_terms * 1.0

	for term in term_counts:
		frequencies[term] = term_counts[term] / all_terms

	return frequencies

# Print dictionary in "key value" format
def printDict(my_dict):
	for item in my_dict:
		print("%s %s" % (item, my_dict[item]))

def main():
	tweets = loadTweets(sys.argv[1])
	term_counts, all_terms = termOccurences(tweets)
	term_freq = termFreq(term_counts, all_terms)
	printDict(term_freq)

if __name__ == '__main__':
	main()
