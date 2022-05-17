# COMP90024 - Assignment 2 - team 60
#
#  Junhong Liu         - Student ID: 1084997 - Melbourne
#  Justin Beaconsfield - Student ID: 761885  - Melbourne
#  Callum Dowling      - Student ID: 1009257 - Palmwoods
#  Soham Swapnil Dighe - Student ID: 1219439 - Melbourne
#  Samy Allouache      - Student ID: 1210426 - Melbourne

import json
import geopandas as gpd
from collections import defaultdict
from shapely.geometry import Point

tweets = []

with open('/Users/justinbeaconsfield/Downloads/smallTwitter.json') as twts:
    i = 0
    for tweet in twts:
        if i != 0:
            ptweet = tweet[:-2]
            if ptweet[-2:] != '}}':
                ptweet = ptweet[:-1]

            tweet_json = json.loads(ptweet)
            tweets.append(tweet_json)

        i += 1

elecs = gpd.read_file("/Users/justinbeaconsfield/Downloads/vic-july-2021-esri/E_VIC21_region.shp")

alp_keywords = {'labor', 'labour', 'alp'}
albanese_keywords = {'albo', 'albanese'}
lnp_keywords = {'liberal', 'libs', 'lnp'}
morrison_keywords = {'scomo', 'morrison'}

def find_elec(point):
    for (poly, name) in zip(elecs.geometry, elecs.Sortname):
        if point.within(poly):
            return poly
    return 'Non Vic'

def check_keywords(keys, text):
    for key in keys:
        if key in text:
            return True
    return False

elec_dict = defaultdict(lambda: defaultdict(int))

for tweet in tweets:
    if tweet['doc']['coordinates'] is not None:
        point = Point(tweet['doc']['coordinates']['coordinates'][0], tweet['doc']['coordinates']['coordinates'][1])

        elec = find_elec(point)
        elec_dict[elec]['count'] += 1

        if check_keywords(alp_keywords, tweet['doc']['text']): elec_dict[elec]['alp'] += 1
        if check_keywords(albanese_keywords, tweet['doc']['text']): elec_dict[elec]['albo'] += 1
        if check_keywords(lnp_keywords, tweet['doc']['text']): elec_dict[elec]['lnp'] += 1
        if check_keywords(morrison_keywords, tweet['doc']['text']): elec_dict[elec]['scomo'] += 1