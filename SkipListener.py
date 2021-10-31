#right this should work
#here goes
import spotipy

import time

from spotipy.oauth2 import SpotifyOAuth

#set keys for spotipy. still cant work out why it needs a redirect and cant just grab the key itself
#saves the key to mem too
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ClientIdKeyHere",
                                               client_secret="ClientSecretHere",
                                               redirect_uri="Redirect_URI",
   	                                           scope="user-modify-playback-state"))
while True:
	with open("counter.txt","r") as f:
		numberOfVotes = f.readlines()
		for line in numberOfVotes:
			if int(line) >= 5:
				sp.next_track()
				print("Skipped!")
				f.close()
				with open("counter.txt","w") as w:
					w.write("0")

			else: 
				continue
		f.close()
		print("file has been closed. this is PHP's window to read, waiting 20")
		time.sleep(10)

	