# Spotify-python-api

Using the QT bus tool qdbus, it is possible to control the spotify client from the command line.

This API maps all possible commands for easy use in python.

I have not been able to find a way to search for tracks or to handle playlists,
so to create a player would require some other way of retrieving that information.

# Problems

Calling spotifyPlay(link to song here) plays a track, however it plays only that track and does not continue playing the playlist.

There is no way to queue tracks, so you would have to build your own playlist and manually play tracks.

Finding the length of a track is possible, however seeking or finding current position in tracks is not. 
