from spotifyqt import *




#reactorUri = "spotify:track:3fWGoSGKD4vA2ty56qEIxR"


"""
def event():
  print("Welcome to CLI Spotify 0.1")
  answer = ""
  while(answer!='a'):
    while(len(answer)==0 or len(answer)>1):
      answer = input("{}\n{}\n{}\n{}\n{}\n{}\n".format(
        "What do you want to do?",
        "[p]lay a track",
        "[s]top playing",
        "[n]ext track",
        "p[r]evious track:",
        "[t]rack info"))


    if(answer=='p'):
      spotifyPlay()
      print("Now playing: {} - {}".format(spotifyMetadata()["title"], spotifyMetadata()["artist"]))
    elif(answer=='s'):
      spotifyStop()
    elif(answer=='n'):
      spotifyNextTrack()
      print("Skipping track...\nNow playing: {} - {}".format(spotifyMetadata()["title"], spotifyMetadata()["artist"]))
    elif(answer=='r'):
      spotifyPreviousTrack()
      print("Previous track...\nNow playing: {} - {}".format(spotifyMetadata()["title"], spotifyMetadata()["artist"]))
    elif(answer=='t'):
      metadata = spotifyMetadata()
      print("---------Track information-----------")
      print("Track:\t\t\t{}\nArtist:\t\t\t{}\nAlbum:\t\t\t{}\nTrack length:\t\t{}\nRating:\t\t\t{}\n{}\n".format(
             metadata['title'],
             metadata['artist'],
             metadata['album'],
             metadata['length'],
             metadata['autoRating'],
             "-------------------------------------"))
    answer = ""

event()

"""
#spotifySeek(10000000)
#metalol = spotifyMetadata()
#trackid = metalol['trackid']
#position = 100

#print(spotifySetPosition(trackid, position))






class Spotify:
  def __init__(self, artUrl, length, trackid, album, artist, autoRating, title, trackNumber, url):
    self.artUrl = artUrl
    self.length = length
    self.trackid = trackid
    self.album = album
    self.artist = artist
    self.autoRating = autoRating
    self.title = title
    self.trackNumber = trackNumber
    self.url = url

  def getLength(self):
    return self.length

  def printTrack(self):
    print("Title\t\t\t\t\t\tArtist\n{}\t\t-\t\t{}".format(self.title, self.artist))

meta = spotifyMetadata()
spotify = Spotify(meta['artUrl'],meta['length'],meta['trackid'],meta['album'],meta['artist'],meta['autoRating'],meta['title'],meta['trackNumber'],meta['url'])

print(spotify.getLength())
spotify.printTrack()
