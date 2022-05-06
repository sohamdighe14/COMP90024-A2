from lib2to3.pgen2 import token
import tweepy
import configparser
import csv
import pandas as pd
import json
import couchdb
import argparse


"""
MELB_LAT = 	"-37.840935"
MELB_LONG = "144.946457"
RADIUS = "40"
"""


class tweetStorer(tweepy.StreamingClient):

    def __init__(self, bear_tok, tokenNb,database):
        super().__init__(bearer_token=bear_tok)
        self.db = database
        self.tokenNb = tokenNb

    def on_data(self, rawData):
        jsn = json.loads(rawData)
        data = jsn["data"]
        id = data["id"]
        data["id"]="partition:"+id
        data["_id"]=data.pop("id")
        self.db.save(data)

def main(tokensFile):
    couch = couchdb.Server('http://admin:adminpass@172.26.128.198:5984/')
    db = couch["election_tweets"]
    
    tokens = read_bearer_tokens(tokensFile)

    for i in range(len(tokens)):
        try:
            st = generate_tweepy_streamingClient(tokens[i],str(i), db)
            st.filter()
        except Exception:
            print("Streaming client n°"+ str(i)+ " encountered an exception")
            print("Processing tweets with client n°"+ str(i+1))
            continue


def read_bearer_tokens(tokensFile):
    # read in all info associated with each key we will be using to authenticate
    # the tweet harvester
    with open(tokensFile) as f:
        return f.read().splitlines()

def generate_tweepy_streamingClient(bearer_token,tokennb, db):
    # generate a tweepy API to use given access tokens and api keys
    stream = tweetStorer(bear_tok = bearer_token, tokenNb=tokennb, database = db)
    stream.add_rules(tweepy.StreamRule("#auspol lang:en"))
    return stream

"""
def harvest_tweets(key, since_id):
   # harvest tweets that are newer than a particular tweet using a given key
    try:
        
    except tweepy.TweepyException:
        return None
"""  


"""def tweet_harvester(keys):
    # given a list of keys, find a key that can be used to harvest tweets and 
    # harvest as many as we can. If no keys work, sleep for 15 minutes
    for token in tokens:
        st = generate_tweepy_api(token)
        st.filter()
    pass
"""
"""def insert_tweets():
    # insert tweets into a couchDB instance (perhaps do some basic filtering)
    pass
"""
# read configs
"""def somethingelse():
    user = api.get_user(screen_name = "Kage_317")
    ID = user.id_str

    tweets = pd.DataFrame(columns = ["time","content", "name", "location"])

    for tweet in api.user_timeline(user_id = ID, screen_name = "Kage_317"):
        pd_info = pd.DataFrame([[tweet.created_at, tweet.text, tweet.user.screen_name, 
                tweet.user.location]], columns = ["time","content", "name", "location"])
        tweets = pd.concat([tweets, pd_info], ignore_index=True)

    tweets.to_csv("KageTweets.csv")"""

def parseArguments():
    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument("-b", "--bearer_tokens", help="file containing the bearer tokens", type=str, default='./bearer_tokens.txt')

    # Parse arguments
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parseArguments()
    main(args.bearer_tokens)