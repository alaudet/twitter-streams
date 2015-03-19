Simple Twitter stream listeners for various topics I like.
Dumps tweets to a mongo database and then can be exported to csv file for futher analysis.
Converts date to Eastern time.

To use these you must create an account at https://dev.twitter.com.
You must then create an application and generate your keys and fill in the following
variables in the scripts.

- consumer_key=""

- consumer_secret=""

- access_token=""

- access_token_secret=""

Requirements
============
- Mongo-DB database

- Robomongo GUI for Mongo-DB (optional)

- Tweepy

- Pymongo

Analyse.ipynb - Analyse data scraped from twitter.
Requires matplotlib, numpy, pandas, nltk, folium

Search
======

search.py searches all tweets over the past week on a given filter



