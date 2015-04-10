Simple Twitter stream listeners for various topics I like.
Dumps tweets to console and a mongo database for future analysis.

See mongo_db_commands for dumping database to csv if you prefer.

To use these you must create an account at https://apps.twitter.com.
You must then create an application and generate your keys and fill in the following
variables in the scripts.  Your app can be create Read-Only for this.

- consumer_key=""

- consumer_secret=""

- access_token=""

- access_token_secret=""


These scripts use ConfigParser to read the keys instead of putting them directly into the scripts.
Put .tweepy in your home folder and then change the script to point to it. This is a better approach than 
loading keys into scripts so that you don't mess up and upload your keys to Github.

Requirements
============
- Mongo-DB database

- Robomongo GUI for Mongo-DB (optional)

- Tweepy

- Pymongo

Example notebooks to analyse data scraped from twitter.
Requires matplotlib, pandas, nltk, folium

Search
======

search*.py searches all tweets over the past week on a given filter



