import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import re
import random
from tqdm import tqdm

#logIn to API
client_credentials_manager = SpotifyClientCredentials("87b58a021fd44e488b6e0857f67ef780", "a1817896ac4249758675fccd7cc3e7ff")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Open song data database
csvfile = open('songdata.csv', newline='')
data = list(csv.reader(csvfile))


#iterates over db and build request using artist name and title
for _ in range(0,100):
    index = random.randint(1,len(data)-1)
    artist = data[index][0]
    title = data[index][1]
    songsearch = artist + ' ' +  title

    #send request
    song_result = sp.search(q=songsearch, type='track', limit=1)

    try:
        #search for album
        album_uri = song_result['tracks']['items'][0]['album']['uri']
        album_res = sp.album(album_uri)
        genres = album_res['genres']
        print(genres)
    except IndexError as e:
	    print('!############error:' + songsearch)
