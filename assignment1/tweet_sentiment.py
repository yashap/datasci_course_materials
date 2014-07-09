import sys
import csv
# import json

# Generic functions
def lines(fp):
	print str(len(fp.readlines()))
	# Simply prints the number of lines in a file

# Load AFINN file
def loadSentiment(fname):
	scores = {}
	with open(fname, 'rb') as f:
		content = csv.reader(f, delimiter="\t")
		for line in content:
			scores[line[0]] = int(line[1])
	return scores

# Load Tweets

def main():
	sent_file = open(sys.argv[1])
	# tweet_file = open(sys.argv[2])
	lines(sent_file)
	# lines(tweet_file)
	print(loadSentiment("AFINN-111.txt"))

if __name__ == '__main__':
	main()
