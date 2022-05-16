# COMP90024 - Assignment 2 - team 60
#
#  Junhong Liu         - Student ID: 1084997 - Melbourne
#  Justin Beaconsfield - Student ID: 761885  - Melbourne
#  Callum Dowling      - Student ID: 1009257 - Palmwoods
#  Soham Swapnil Dighe - Student ID: 1219439 - Melbourne
#  Samy Allouache      - Student ID: 1210426 - Melbourne

from genericpath import exists
import tweepy
import configparser
import json
import couchdb
import time


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
    db = couch["election_tweets1"]
    api_keys = read_api_keys("./config.ini")
    filtrationList = ["#auspol #melbourne","#auspol #Morisson","#auspol #Albo4PM", "#auspol"]
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
                st.filter(track=filtrationList)
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

if __name__ == "__main__":
    main()