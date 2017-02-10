# coding=utf-8

from subprocess import *
import os
import sys
import errno
import time
import re


qdbus = "qdbus"
##Defensive coding should have tests for qdbus version and so on.

arg1 = 'org.mpris.MediaPlayer2.spotify'
arg2 = '/org/mpris/MediaPlayer2'
arg3 = 'org.mpris.MediaPlayer2.Player'

##if called with empty brackets it will just resume playback
##if called with a spotify uri as an argument it will play that song
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

def spotifyPlayPause():
    cmd = Popen((qdbus,arg1,arg2, arg3+'.PlayPause'), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, errors = cmd.communicate(b"")
    if (errors):
      exit(errors)

def spotifyStop():
    cmd = Popen((qdbus,arg1,arg2, arg3+'.Stop'), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, errors = cmd.communicate(b"")
    if (errors):
      exit(errors)

def spotifyMetadata():
    cmd = Popen((qdbus,arg1,arg2,'org.freedesktop.DBus.Properties.Get', arg3,'Metadata'), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, errors = cmd.communicate(b"")
    if (errors):
      exit(errors)
    else:
      print(output)



##INTERFACE##
#spotifyPlay('spotify:track:2QePQ29ix8gC0CbRHcGoBz') #byter till G Jones - Zig Zak
#spotifyPlay() #Spelar oavsett om den redan spelar eller är tyst
#spotifyPlayPause() #Byter mellan paus och play
#spotifyMetadata() #Ger tillbaka massa metadata som går att använda
spotifyStop()
