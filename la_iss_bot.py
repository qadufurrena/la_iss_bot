import json
import urllib.request
import os
from os import environ
import math
import tweepy as tp
from time import sleep

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['acces_token']
access_secret = environ['access_secret']

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

text = "Look to the skies! The ISS is over Los Angeles"

#center_lon and center_lat Griffith Observatory coordinates, center_lon = -118.30043
    #center_lat = 34.11843
#latitude: 1 deg = 110.574km
#longitude: 1 deg = 111.320*cos(latitude)km
#radius of visibility = 2316.4km 
#initiate thrusters!

while True:
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    R = 2316.4
    center_lon = -118.30043
    center_lat = 34.11843
    Rlat = abs((center_lat-lat) * 110.574)
    Rlon = abs((center_lon-lon) * (111.320 * math.cos(lat)))
    while Rlat > R or Rlon > R:
        print("nope")
        sleep(5)
    else:
        api.update_status(text)
        print("It's here!")
        sleep(1800)
        





