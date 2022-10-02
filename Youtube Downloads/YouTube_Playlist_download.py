# CODE FOR DOWNLOADING COMPLETE PLAY LIST OF YOUTUBE VIDEOS 

from pytube import Playlist

URL_link = input("Enter playlist URL :")
PLAYLIST = Playlist(URL_link)

print(f'Downloading : {PLAYLIST.title}')

for video in PLAYLIST.videos:
   video.streams.get_highest_resolution().download()

print("Playlist Sucessfully Downloaded")   