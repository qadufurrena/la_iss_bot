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

while True:
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    R = 1774.5
    center_lon = -118.30043
    center_lat = 34.11843
    x = lon
    y = lat
    Rlat = abs((center_lat-y) * 110.574)
    Rlon = abs((center_lon-x) * (111.320 * math.cos(y*0.01745329)))
    C = (math.sqrt(((Rlat) ** 2) + ((Rlon) ** 2)))

while True:
    now_hour = int(datetime.now().strftime('%H'))
    
    if now_hour >= 20 and now_hour <= 23:
        (lat, lon) = current_position('http://api.open-notify.org/iss-now.json')

        Rlat = abs((center_lat-lat) * 110.574)
        Rlon = abs((center_lon-lon) * (111.320 * math.cos(lat*0.01745329)))
        C = (math.sqrt(((Rlat) ** 2) + ((Rlon) ** 2)))
        
        if C <= R:
            print("It's here!", "lat:", lat, "lon:", lon, "Rlat:", Rlat, "Rlon:", Rlon, "C:", C)
            api.update_status(text)
            sleep(1800)
        else:
            print("nope", "lat:", lat, "lon:", lon, "Rlat:", Rlat, "Rlon:", Rlon, "C:", C)
            sleep(1)
    else: 
        print('not here')
        sleep(5)





