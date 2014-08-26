#!/usr/bin/python
# Get the last 7 days of tweets by keyword


import tweepy
import pymongo

consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
db = pymongo.MongoClient().timmins

for status in tweepy.Cursor(api.search,
                           q="Timmins",
                           count=100,
                           result_type='recent',
                           include_entities=True,
                           monitor_rate_limit=True, 
                           wait_on_rate_limit=True,
                           lang="en").items():
    print status.created_at,
    print "--- ",
    print status.user.name,
    print status.user.screen_name,
    print "--- ",
    print status.user.location,
    print "--- ",
    print status.text,
    print status.coordinates,
    print status.source
    print ""
    data ={}
    data['name'] = status.user.name
    data['screen_name'] = status.user.screen_name
    data['location'] = status.user.location
    data['text'] = status.text
    data['created_at'] = status.created_at
    data['geo'] = status.coordinates
    data['source'] = status.source

    db.Tweets.insert(data)

