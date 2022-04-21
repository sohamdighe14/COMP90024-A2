import tweepy
import configparser
import csv

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

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

csvFile = open("KageTweets2.csv", 'a')
csvWriter = csv.writer(csvFile)

for tweet in api.user_timeline(user_id = ID, screen_name = "Kage_317"):
    csvWriter.writerow([tweet.created_at, tweet.text, 
                        tweet.user.screen_name, 
                        tweet.user.location])