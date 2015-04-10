#!/usr/bin/python
# Get the last 7 days of tweets by keyword


import tweepy
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

db = pymongo.MongoClient().jays1week_from_2015_03_18

for status in tweepy.Cursor(api.search,
                           q="#BlueJays",
                           count=100,
                           result_type='recent',
                           include_entities=True,
                           monitor_rate_limit=True, 
                           wait_on_rate_limit=True,
                           lang="en").items():
    print status.created_at 
    # utc_time = dateutil.parser.parse(status.created_at)
    # print utc_time
    eastern_time = status.created_at - timedelta(hours=4)
    edt_time = eastern_time.strftime('%Y-%m-%d %H:%M')

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
    data = {}
    data['name'] = status.user.name
    data['screen_name'] = status.user.screen_name
    data['location'] = status.user.location
    data['text'] = status.text
    data['created_at'] = edt_time
    data['geo'] = status.coordinates
    data['source'] = status.source

    db.Tweets.insert(data)
