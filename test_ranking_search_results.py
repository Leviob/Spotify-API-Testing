#! /usr/bin/python3

#TODO: iterate results looking for exact matches and push them to the top of the results

from dotenv import load_dotenv
load_dotenv()
import os, spotipy
from spotipy.oauth2 import SpotifyClientCredentials
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))
query = 'circ'
results = sp.search(q=query, limit=10)

ranked = {}
for result in results['tracks']['items'][0]['artists']:
    if result['name'] == query:
        ranked['name'] = result

print(ranked)

# for track in results['tracks']['items']:
#     print(track['artists'][0]['name'])

# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])