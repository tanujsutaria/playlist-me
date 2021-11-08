from urllib.parse import scheme_chars
from flask import Flask
import spotipy
from spotipy import oauth2
from Meta import auth_constants

sp_auth = oauth2.SpotifyOAuth( auth_constants.SPOTIFY_CLIENT_ID, 
auth_constants.SPOTIFY_CLIENT_SECRET, auth_constants.SPOTIFY_REDIRECT_URI,
scope=auth_constants.SCOPE, cache_path=auth_constants.CACHE )

