import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

jeremy_uri = 'spotify:artist:77yY2QmM6bYvjJ3y5L2R0v'

client_credentials_manager = SpotifyClientCredentials('b2242e9dfe6140c0a8c6f06c9f36c5ae',
                                                      'b5acdfd6ef904416ad89dad12b8ba89f')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# artist = sp.artist(jeremy_uri)
# print(artist)

results = sp.artist_albums(jeremy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
