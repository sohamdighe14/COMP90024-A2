import tweepy
import configparser
import csv
import pandas as pd


MELB_LAT = 	-37.840935
MELB_LONG = 144.946457
RADIUS = 40


def read_api_keys(config_file):
    # read in all info associated with each key we will be using to authenticate
    # the tweet harvester
    config = configparser.ConfigParser()
    config.read(config_file)
    keys = dict()
    for item in config.sections():
        keys[str(item)] = config[item]
    return keys

def generate_tweepy_api(key):
    # generate a tweepy API to use given access tokens and api keys
    api_key = key["api_key"]
    api_key_secret = key["api_key_secret"]
    access_token = key["access_token"]
    access_token_secret = key["access_token_secret"]
    auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, 
                                    access_token_secret)
    api = tweepy.API(auth)
    return api

def harvest_tweets(key, since_id):
    # harvest tweets that are newer than a particular tweet using a given key
    try:
        api = generate_tweepy_api(key)
    except tweepy.TweepyException:
        return None
    
def tweet_harvester(keys):
    # given a list of keys, find a key that can be used to harvest tweets and 
    # harvest as many as we can. If no keys work, sleep for 15 minutes
    pass

def insert_tweets():
    # insert tweets into a couchDB instance (perhaps do some basic filtering)
    pass

# read configs
def somethingelse():
    user = api.get_user(screen_name = "Kage_317")
    ID = user.id_str

    tweets = pd.DataFrame(columns = ["time","content", "name", "location"])

    for tweet in api.user_timeline(user_id = ID, screen_name = "Kage_317"):
        pd_info = pd.DataFrame([[tweet.created_at, tweet.text, tweet.user.screen_name, 
                tweet.user.location]], columns = ["time","content", "name", "location"])
        tweets = pd.concat([tweets, pd_info], ignore_index=True)

    tweets.to_csv("KageTweets.csv")