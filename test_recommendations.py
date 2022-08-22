#! /usr/bin/python3
import pprint
from dotenv import load_dotenv
load_dotenv()
import os, spotipy
from spotipy.oauth2 import SpotifyClientCredentials
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))

results = sp.recommendations(seed_artists=['https://open.spotify.com/artist/3jOstUTkEu2JkjvRdBA5Gu'], limit=1, country='US')
pprint.pprint(results)

# recommendations(seed_artists='', seed_genres=None, seed_tracks=None, limit=20, country=None, **kwargs)