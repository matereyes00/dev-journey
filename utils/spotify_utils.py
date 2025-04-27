import spotipy
from dotenv import load_dotenv
import os
import re
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope="playlist-read-private"
))


def extract_playlist_id(playlist_url):
    match = re.search(r'playlist/([a-zA-Z0-9]+)', playlist_url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Spotify playlist URL")


def get_playlist_tracks(playlist_url):
    playlist_id = extract_playlist_id(playlist_url)
    results = sp.playlist_tracks(playlist_id)
    tracks = []

    for item in results['items']:
        track = item['track']
        if not track:  # Sometimes track is None
            continue
        artist = track['artists'][0]
        audio_features = sp.audio_features([track['id']])[0]
        artist_info = sp.artist(artist['id'])
        genres = artist_info['genres']

        track_data = {
            'name': track['name'],
            'artist': artist['name'],
            'genres': genres,
            'valence': audio_features['valence'],
            'energy': audio_features['energy'],
            'danceability': audio_features['danceability']
        }
        tracks.append(track_data)

    return tracks