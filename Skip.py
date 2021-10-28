'''
This is the script that actually calls the API to skip the song
AS much as PHP is a good language API calls are so much easier using python libraries
big up
'''
#import libraries
import spotipy

from flask import Flask, request

from spotipy.oauth2 import SpotifyOAuth

#set keys for spotipy. still cant work out why it needs a redirect and cant just grab the key itself
#saves the key to mem too
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="1aa9cf575d0c4a9ba499577e31c2718c",
                                               client_secret="970b1b03db8f4c28bec0ba992aadc695",
                                               redirect_uri="http://dansilver.uk/",
                                               scope="user-modify-playback-state"))
sp.next_track()

#hi this next bit is commented out because it doesnt work yet
#this code needs to accept a post request from the php script that will then
#trigger the api call to skip the song.
#this still doesnt have a counter in it
#but the counter should count the amount of post requests its recieved since
#uptime and then do that shit after 5 recieved, and then clear counter


'''
app = Flask(__name__)
@app.route('/',methods=['POST'])
def result():
    Recieved = False
    while True:
        if recieved == True:
            sp.next_track()
            break
'''







