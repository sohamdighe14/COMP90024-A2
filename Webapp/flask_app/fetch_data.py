import couchdb
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
couch = couchdb.Server('http://admin:adminpass@172.26.128.198:5984/')

def flatten_doc_2022(doc):
    fdoc=list(dict())
    for d in doc:
        tmp={}
        tmp["id_str"] = d['id_str']
        tmp["text"] = d['text']
        tmp["created_at"] = d["created_at"]
        tmp["rt_counts"] = d['retweet_count']
        tmp["fav_counts"] = d['favorite_count']
        tmp["is_quote_status"] = d['is_quote_status']
        tmp["quote_count"] = d['quote_count']
        tmp["reply_count"] = d['reply_count']
        tmp["lang"] = d['lang']
        tmp["followers"] = d['user']['followers_count']
        tmp["friends"] = d['user']['friends_count']
        tmp["lang"] = d['user']['lang']
        tmp["user_created_at"] = d['user']['created_at']
        tmp["screen_name"] = d['user']['screen_name']
        tmp["user_id"] = d['user']['id']
        tmp["hashtags"] = [x['text'] for x in d['entities']['hashtags']]
        fdoc.append(tmp)
    return fdoc

def get_election_data_2022():
    db = couch["election_tweets1"]
    mango = {
            "selector": {},
            "fields": [
                "id_str",
                "text",
                "created_at",
                "retweet_count",
                "favorite_count",
                "is_quote_status",
                "quote_count",
                "reply_count",
                "lang",
                "user.followers_count",
                "user.friends_count",
                "user.lang",
                "user.created_at",
                "user.location",
                "user.screen_name",
                "user.id",
                "entities.hashtags"
            ],
            "limit": 10000000
            }
    document=list()
    for doc in db.find(mango):
        document.append(dict(doc))

    x = flatten_doc_2022(document)
    tweets = pd.DataFrame(x)
    tweets.to_json('election_data_2022.json')
    
def get_housing_data():
    db = couch["election_tweets1"]
    mango = {
            "selector": {},
            "fields": [
                "id_str",
                "text",
                "created_at",
                "retweet_count",
                "favorite_count",
                "is_quote_status",
                "quote_count",
                "reply_count",
                "lang",
                "user.followers_count",
                "user.friends_count",
                "user.lang",
                "user.created_at",
                "user.location",
                "user.screen_name",
                "user.id",
                "entities.hashtags"
            ],
            "limit": 10000000
            }
    document=list()
    for doc in db.find(mango):
        document.append(dict(doc))

    x = flatten_doc_2022(document)
    tweets = pd.DataFrame(x)
    tweets.to_json('election_data_2022.json')