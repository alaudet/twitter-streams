#!/usr/bin/python

import tweepy
import sys
import pymongo
import datetime
from datetime import timedelta

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

        self.db = pymongo.MongoClient().habs



    def on_status(self, status):
        eastern_time = status.created_at - timedelta(hours=4)
        edt_time = eastern_time.strftime('%Y-%m-%d %H:%M:%S')
        db_time = eastern_time.strftime('%H:%M')
        print edt_time,
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
        data['time'] = db_time
        data['geo'] = status.coordinates
        data['source'] = status.source

        self.db.Tweets.insert(data)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

try:
    sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
    sapi.filter(track=['#GoHabsGo'])
except KeyboardInterrupt:
    print "Stream Killed"
