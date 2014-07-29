#!/usr/bin/python

import tweepy
import sys
import pymongo
import time

consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.db = pymongo.MongoClient().bosox

    def on_status(self, status):
        print status.user.name,
        print "--- ",
        print status.text,
        print time.strftime("%H:%M:%S")
        data ={}
        data['name'] = status.user.name
        data['text'] = status.text
        data['time'] = time.strftime("%H:%M")
        data['geo'] = status.geo
        data['source'] = status.source

        self.db.Tweets.insert(data)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
#setTerms = ['bluejays', 'yankees']
sapi.filter(track=['bluejays'])
