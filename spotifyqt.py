# coding=utf-8

from subprocess import *
import os
import sys
import errno
import time
import re
import curses


##INTERFACE##
#spotifyPlay('spotify:track:2QePQ29ix8gC0CbRHcGoBz') #byter till G Jones - Zig Zak
#spotifyPlay() #Spelar oavsett om den redan spelar eller är tyst
#spotifyPlayPause() #Byter mellan paus och play
#spotifyMetadata() #Ger tillbaka massa metadata som går att använda
#spotifyStop()



#--------------------------------------------
qdbus = "qdbus"
##Defensive coding should have tests for qdbus version and so on.

arg1 = 'org.mpris.MediaPlayer2.spotify'
arg2 = '/org/mpris/MediaPlayer2'
arg3 = 'org.mpris.MediaPlayer2.Player'


def spotifyMethod(method):
    if(method==""):
      return
    cmd = Popen((qdbus,arg1,arg2, arg3+'.{}'.format(method)), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, errors = cmd.communicate(b"")
    if (errors):
      exit(errors)
    else:
      return output

""" spotifyPlay
Purpose: Playing/Resuming playback of a track
         Takes a URI or a HTTP link as an argument.
EXAMPLES: spotifyPlay(https://open.spotify.com/track/3XNhUO3VysNZUGq3Z16SWZ)
Returns: Nothing
if called with empty brackets it will just resume playback
if called with a spotify uri as an argument it will play that song
Precondition: valid uri
"""
def spotifyPlay(uri=None):
  if uri is None:
    cmd = Popen((qdbus,arg1,arg2, arg3+'.Play'), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, errors = cmd.communicate(b"")
    if (errors):
      exit(errors)
  else:
    cmd = Popen((qdbus,arg1,arg2, arg3+'.OpenUri', uri), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, errors = cmd.communicate(b"")
    if (errors):
      exit(errors)


""" spotifyPlayPause
Purpose: If the track is playing, this function pauses it. 
         If the track is paused, this function resumes it.
Returns: Nothing
"""
def spotifyPlayPause():
    cmd = Popen((qdbus,arg1,arg2, arg3+'.PlayPause'), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, errors = cmd.communicate(b"")
    if (errors):
      exit(errors)

""" spotifyStop
Purpose: Pauses the track.
Returns: Nothing
"""
def spotifyStop():
    cmd = Popen((qdbus,arg1,arg2, arg3+'.Stop'), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, errors = cmd.communicate(b"")
    if (errors):
      exit(errors)
      return -1
    return 0

def spotifyNextTrack():
    spotifyMethod("Next")

def spotifyPreviousTrack():
    spotifyMethod("Previous")

"""spotifySetPosition (Not working)


"""
def spotifySetPosition(trackid, position):
    spotifyMethod("SetPosition")

"""spotifySeek (Not working)

"""
def spotifySeek(forwardTime):
    return spotifyMethod("Seek")




"""
metadataRowParse
Purpose: Used to get information for spotifyMetadata()
"""
def metadataRowParse(text):
    col_cnt = 0
    pos = 2
    for character in text:
      if(character==':'):
        col_cnt+=1
      if(col_cnt==2):
        return text[pos:]
      pos+=1


"""
spotifyMetadata
Purpose: Get information about the song currently playing
Returns: Dictionary containing these keys:
          artUrl      - url for album art
          length      - length of song
          trackid     - spotify:track:IDHERE
          album       - (string)
          albumArtist - the artist publishing the album
                        (differs from artist, since an artist 
                        may appear on another artists album)
          artist      - the artist who made the song
          autoRating  - some rating system, (double)
          discNumber  - (int)
          title       - Song title
          trackNumber - (int)
          url         - https link to the song
"""
def spotifyMetadata():
    metadata = {}
    cmd = Popen((qdbus,arg1,arg2,'org.freedesktop.DBus.Properties.Get', arg3,'Metadata'), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, errors = cmd.communicate(b"")
    if (errors):
      exit(errors)
    else:
      metasplit = output.decode('utf-8').split('\n')
      for i, row in enumerate(metasplit):
        if(len(row.split(':'))>2):
          metadata[row.split(':')[1]] = metadataRowParse(row)
    return metadata



#EOF
