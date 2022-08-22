#! /usr/bin/python3
from dotenv import load_dotenv
load_dotenv()
import os, spotipy
from spotipy.oauth2 import SpotifyClientCredentials
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

results = sp.search(q='circ', type='artist', offset=50, limit=50)

for idx, artist in enumerate(results['artists']['items']):
    print(idx, artist['name'])

# Why is Circ the 75th result when searching for 'circ'???