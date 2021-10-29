'''
This is the script that actually calls the API to skip the song
AS much as PHP is a good language API calls are so much easier using python libraries
big up
'''
#import libraries
import spotipy

from spotipy.oauth2 import SpotifyOAuth

#set keys for spotipy. still cant work out why it needs a redirect and cant just grab the key itself
#saves the key to mem too
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="APP_CLIENT_ID",
                                               client_secret="APP_CLIENT_SECRET",
                                               redirect_uri="REDIRECT_URI",
                                               scope="user-modify-playback-state"))

#spotipy function call
sp.next_track()







