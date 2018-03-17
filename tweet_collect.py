import tweepy
from time import sleep
from credentials import *
import pandas as pd

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# twitter_data = pd.DataFrame(columns = ["id", "tm", "screen_name", "text"])

# From tweets that have mentioned me

def collect_tweets(screen_name , last_tweet, api):
	tweets = []
	for tweet in api.search(q=screen_name, since_id=last_tweet):
		record = {}
		record["id"] = tweet.id
		record["tm"] = 't'
		record["screen_name"] = tweet.user.screen_name
		record["text"] = tweet.text
		tweets.append(record)
	df = pd.DataFrame(tweets)
	return df


def collect_messages(since, api):
	messages = []
	for message in api.direct_messages(since_id=since):
		record = {}
		record["id"] = message.id
		record["tm"] = 'm'
		record["screen_name"] = message.sender.screen_name
		record["text"] = message.text
		messages.append(record)
	df = pd.DataFrame(messages)
	return df


def write_tweet_messages(screen_name, last_tweet, last_message, outfile, api):
	df = collect_tweets(screen_name,last_tweet,api)
	df2 = collect_messages(last_message,api)
	result = [df,df2]
	result = pd.concat(result)
	with open(outfile, 'w') as f:
		result.to_csv(f, index = False)
		# header = False, columns = ['id','screen_name','text','tm','result']