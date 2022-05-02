import tweepy
import configparser
import csv
import pandas as pd


def read_api_keys(config_file):
    # read in all info associated with each key we will be using to authenticate
    # the tweet harvester
    config = configparser.ConfigParser()
    config.read(config_file)
    keys = dict()
    for item in config.sections():
        keys[str(item)] = config[item]
    return keys

def generate_auth(key):
    # given a particular key info, generate an api for the key
    pass

def tweet_harvester(keys):
    # given a list of keys, find a key that can be used to harvest tweets and 
    # harvest as many as we can. If no keys work, sleep for 15 minutes
    pass

def insert_tweets():
    # insert tweets into a couchDB instance (perhaps do some basic filtering)

# read configs
def somethingelse():
    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']

    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    # authentication
    auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, 
                                    access_token, access_token_secret)
    api = tweepy.API(auth)

    user = api.get_user(screen_name = "Kage_317")
    ID = user.id_str

    tweets = pd.DataFrame(columns = ["time","content", "name", "location"])

    for tweet in api.user_timeline(user_id = ID, screen_name = "Kage_317"):
        pd_info = pd.DataFrame([[tweet.created_at, tweet.text, tweet.user.screen_name, 
                tweet.user.location]], columns = ["time","content", "name", "location"])
        tweets = pd.concat([tweets, pd_info], ignore_index=True)

    tweets.to_csv("KageTweets.csv")
