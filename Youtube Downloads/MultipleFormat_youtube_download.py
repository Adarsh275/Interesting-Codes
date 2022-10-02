from ast import For
from random import choices
from pytube import YouTube

link = input(" Enter Your URL :")
video = YouTube(link)

print(video.title)

List_videos = video.streams.all()
# List_videos = video.streams.filter(only_audio=True) # only audio list will be displayed
vid = list(enumerate(List_videos))

for i in vid:
   print (i)
print()

Choice = int(input("Enter video No :"))
List_videos[Choice].download()
print("your video downloaded sucessfully")