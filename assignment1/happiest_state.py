import sys
import csv
import json

# Designed to be run from terminal, with this command:
# python happiest_state.py AFINN-111.txt output.txt

# Dictionary of states:
states = {
	"AK": "Alaska",
	"AL": "Alabama",
	"AR": "Arkansas",
	"AS": "American Samoa",
	"AZ": "Arizona",
	"CA": "California",
	"CO": "Colorado",
	"CT": "Connecticut",
	"DC": "District of Columbia",
	"DE": "Delaware",
	"FL": "Florida",
	"GA": "Georgia",
	"GU": "Guam",
	"HI": "Hawaii",
	"IA": "Iowa",
	"ID": "Idaho",
	"IL": "Illinois",
	"IN": "Indiana",
	"KS": "Kansas",
	"KY": "Kentucky",
	"LA": "Louisiana",
	"MA": "Massachusetts",
	"MD": "Maryland",
	"ME": "Maine",
	"MI": "Michigan",
	"MN": "Minnesota",
	"MO": "Missouri",
	"MP": "Northern Mariana Islands",
	"MS": "Mississippi",
	"MT": "Montana",
	"NA": "National",
	"NC": "North Carolina",
	"ND": "North Dakota",
	"NE": "Nebraska",
	"NH": "New Hampshire",
	"NJ": "New Jersey",
	"NM": "New Mexico",
	"NV": "Nevada",
	"NY": "New York",
	"OH": "Ohio",
	"OK": "Oklahoma",
	"OR": "Oregon",
	"PA": "Pennsylvania",
	"PR": "Puerto Rico",
	"RI": "Rhode Island",
	"SC": "South Carolina",
	"SD": "South Dakota",
	"TN": "Tennessee",
	"TX": "Texas",
	"UT": "Utah",
	"VA": "Virginia",
	"VI": "Virgin Islands",
	"VT": "Vermont",
	"WA": "Washington",
	"WI": "Wisconsin",
	"WV": "West Virginia",
	"WY": "Wyoming"
}

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

def tweetScore(tweet, scores):
	tweet_score = 0
	words = tweet.split()
	for word in words:
		word_score = scores.get(word)
		if not word_score:
			word_score = 0
		tweet_score += word_score
	return tweet_score

def scoreStates(tweets, scores):
	state_scores = {}
	for tweet in tweets:
		text = tweet.get("text")
		place = tweet.get("place")
		if text and place and place["country_code"] == "US":
			place_name = place["full_name"]
			for state in states:
				if state in place_name or states[state] in place_name:
					if state in state_scores:
						state_scores[state] += tweetScore(text, scores)
					else:
						state_scores[state] = tweetScore(text, scores)
	return state_scores

def happiestState(state_scores):
	happiest = ["None", -9999999999]
	for state in state_scores:
		if state_scores[state] > happiest[1]:
			happiest[0] = state
			happiest[1] = state_scores[state]
	return happiest[0]

def main():
	scores = loadSentiment(sys.argv[1])
	tweets = loadTweets(sys.argv[2])
	state_scores = scoreStates(tweets, scores)
	print(happiestState(state_scores))

if __name__ == '__main__':
	main()
