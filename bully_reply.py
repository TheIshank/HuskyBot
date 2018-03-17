import pandas as pd
import tweepy
from tweet_collect import *
from credentials import *
from sklearn.externals import joblib
import json

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler = auth, wait_on_rate_limit=True, compression = True)

outfile = 'tweets_messages.csv'

with open("config.json") as json_file:
	config_data = json.load(json_file)

# print(json_data['screen_name'])

write_tweet_messages(screen_name = api.me().screen_name, last_tweet = config_data['last_tweet'], last_message = config_data['last_message'], outfile = outfile, api = api)
data = pd.read_csv(outfile)
model_file = 'finalized_model.sav'
X = data['text']
loaded_model = joblib.load(model_file)
result = loaded_model.predict(X)
data['result'] = result

data.to_csv("results.csv")

message = "We have detected that you have tried to bully @"+ api.me().screen_name+". Please refrain from such behaviour in future.\nYou wrote: "

for i,row in data.loc[data.result == 1].iterrows():
	if(row['tm'] == 't'):
		sent_message = message+row['text']+" \nOn: "+str(api.get_status(row['id']).created_at)
	else:
		sent_message = message+row['text']+" \nOn: "+str(api.get_direct_message(row['id']).created_at)
	print(row['screen_name'], " ", sent_message)
	if(row['tm'] == 'm'):
		config_data['last_message'] = row['id']
	else:
		config_data['last_tweet'] = row['id']
	api.send_direct_message(screen_name = row['screen_name'], text = sent_message)

with open('config.json', 'w') as json_file:
    json.dump(config_data, json_file)