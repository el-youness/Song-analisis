import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import re
from tqdm import tqdm

#logIn to API
client_credentials_manager = SpotifyClientCredentials("87b58a021fd44e488b6e0857f67ef780", "a1817896ac4249758675fccd7cc3e7ff")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Open song data database
csvfile = open('songdata.csv', newline='')
data = list(csv.reader(csvfile))

with open('yearsAndGenre.csv', 'w') as csvfile:
infoWriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
infoWriter.writerow(['release_year', 'genre'])
x,y=0

#iterates over db and build request using artist name and title
for i in tqdm(range(1,len(data))):
	artist = data[i][0]
    title = data[i][1]
    info = []

	#send request
    songsearch = artist + ' ' +  title
	song_result = sp.search(q=songsearch, type='track', limit=1)
	try:
		#search for year only
		years = re.findall("\d{4}", song_result['tracks']['items'][0]['album']['release_date'])
	except IndexError as e:
		j+=1
        years = -1
        
    try:
	    #search for album
	    uri = song_result['tracks']['items'][0]['album']['uri']
	    album = sp.album(uri)

	except IndexError as e:
    albumsearch = artist + ' ' + album
    album_result = sp.search(q=albumsearch, type='album', limit=1)

print("number tracks not found on spotify = "+ str(j))
file.close();
