from genericpath import exists
import tweepy
import configparser
import pandas as pd
import json
import couchdb
import time


"""
MELB_LAT = 	"-37.840935"
MELB_LONG = "144.946457"
RADIUS = "40"
"""




class listener(tweepy.Stream):

    def __init__(self, key, database):
        api_key = key["api_key"]
        api_key_secret = key["api_key_secret"]
        access_token = key["access_token"]
        access_token_secret = key["access_token_secret"]
        super().__init__(api_key, api_key_secret,access_token,access_token_secret)
        self.db = database

    def on_data(self, data):
        jsn = json.loads(data)
        id = str(jsn["id"])
        jsn["id"]="partition:"+id
        jsn["_id"]=jsn.pop("id")
        self.db.save(jsn)
        return(True)

    def on_error(self, status):
        print(status)

def main():
    couch = couchdb.Server('http://admin:adminpass@172.26.128.198:5984/')
    db = couch["election_tweets2"]
    api_keys = read_api_keys("./config.ini")
    firstIteration = True
    timers=[]

    print(api_keys.values())

    for key in api_keys.values():
        timers.append(time.time())

    while True:   
        currentStream=0

        for key in api_keys.values():
            print(currentStream)
            try:
                if not(firstIteration):
                    loopTime = time.time()-timers[currentStream]
                    if loopTime < 900:
                        time.sleep(900-loopTime)
                    firstIteration=False
                
                st = listener(key, db)
                st.filter(track=["#auspol #melbourne"])
            except Exception:
                print("Streaming client n°"+ str(currentStream)+ " encountered an exception")
                print("Processing tweets with client n°"+ str(currentStream+1))
                timers[currentStream]= time.time()
                currentStream+=1
                continue

def read_api_keys(config_file):
    # read in all info associated with each key we will be using to authenticate
    # the tweet harvester
    config = configparser.ConfigParser()
    config.read(config_file)
    keys = dict()
    for item in config.sections():
        keys[str(item)] = config[item]
    return keys


"""def read_bearer_tokens(tokensFile):
    # read in all info associated with each key we will be using to authenticate
    # the tweet harvester
    with open(tokensFile) as f:
        return f.read().splitlines()"""

"""def generate_tweepy_streamingClient(bearer_token,tokennb, db):
    # generate a tweepy API to use given access tokens and api keys
    stream = tweetStorer(bear_tok = bearer_token, tokenNb=tokennb, database = db)
    stream.add_rules(tweepy.StreamRule("#auspol lang:en"))
    return stream"""

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

"""def parseArguments():
    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument("-b", "--bearer_tokens", help="file containing the bearer tokens", type=str, default='./bearer_tokens.txt')

    # Parse arguments
    args = parser.parse_args()
    return args"""

if __name__ == "__main__":
    main()