import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import re
import json

client_credentials_manager = SpotifyClientCredentials("87b58a021fd44e488b6e0857f67ef780", "a1817896ac4249758675fccd7cc3e7ff")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Open song data database
csvfile = open('songdata.csv', newline='')
data = list(csv.reader(csvfile))

file = open("dateBySong.txt","w")

j=0

#iterates over db and build request using artist name and title
for i in range(1,200):

	songsearch = data[i][0] + ' ' + data[i][1] #artist + title

	#send request
	results = sp.search(q=songsearch, type='track', limit=1)

	try:
		#search for year only
		years = re.findall("\d{4}", results['tracks']['items'][0]['album']['release_date'])
		print(songsearch+ " -" + years[0])

		file.write(years[0]+",")
	except KeyError as e:
		print('!############error:' + songsearch)
		j+=1
		file.write("-1,")
		#print('I got a KeyError - reason' + str(e))
	except IndexError as e:
		j+=1
		print('!############error:' + songsearch)
		file.write("-1,")
		#print('I got an IndexError - reason' + str(e))


print("number tracks not found on spotify = "+ str(j))
file.close();