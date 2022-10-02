from pytube import YouTube

link = input(" Enter Your URL :")
# link = ""  # hard code your URL in brackets 
video = YouTube(link)
print(video.title)  
# print(video.thumbnail_url) # it will give the thumbnail pic url. 

Stream = video.streams.get_highest_resolution()  # get highest resolution video only
Stream.download()

print("Video Downloaded Sucessfully")