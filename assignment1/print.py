import urllib
import json

response = urllib.urlopen("https://api.twitter.com/1.1/search/tweets.json?q=microsoft")
pyresponse = json.load(response)
print type(pyresponse)
print pyresponse["errors"]
print type(pyresponse["errors"])
print pyresponse["errors"][0].keys()
print pyresponse["errors"][0]["message"]
print type(pyresponse["errors"][0]["message"])