#!/usr/bin/python

import tweepy
import sys
import pymongo
from datetime import timedelta
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/al/.tweepy')

configs = {'consumer_key': config.get('oauth', 'consumer_key'),
           'consumer_secret': config.get('oauth', 'consumer_secret'),
           'access_token': config.get('oauth', 'access_token'),
           'access_token_secret': config.get('oauth', 'access_token_secret')
           }

auth = tweepy.OAuthHandler(configs['consumer_key'], configs['consumer_secret'])
auth.set_access_token(configs['access_token'], configs['access_token_secret'])
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.db = pymongo.MongoClient().yankees_opener



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
    sapi.filter(track=['Yankees'])
except KeyboardInterrupt:
    print "Stream Killed"
