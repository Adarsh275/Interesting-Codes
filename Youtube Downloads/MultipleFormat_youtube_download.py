from pytube import YouTube

link = input("Enter Your URL: ")
video = YouTube(link)
print("VIDEO TITLE: ",video.title)

# List_videos = video.streams.all() # this will list all the types of formate avilable 

while(1) :
   print("\nChoose From the below Options")
   print("1. All video file format \n2. All Only video file format \n3. All Audio file format \n4. Exit Program")
   choose = int(input("Enter your choice : "))

   if choose == 1:
      List_videos = video.streams.filter(progressive=True)
      vid = list(enumerate(List_videos))

      for i in vid:
         print(i)
      print()
            
      Choice = int(input("Enter your preferred resolution No : "))
      List_videos[Choice].download()
      print("your video downloaded sucessfully")

   elif choose == 2:
      List_videos_Only = video.streams.filter(only_video=True)
      vid = list(enumerate(List_videos_Only))

      for i in vid:
         print(i)
      print()
      
      Choice = int(input("Enter your preferred resolution No : "))
      List_videos_Only[Choice].download()
      print("your video downloaded sucessfully")

   elif choose == 3:
      List_audios = video.streams.filter(only_audio=True)   
      aud = list(enumerate(List_audios))

      for i in aud:
         print(i)
      print()

      Choice = int(input("Enter your preferred audio format No : "))
      List_audios[Choice].download()
      print("your audio file downloaded sucessfully")

   elif choose == 4:
      exit()

   else :
      print("Please Enter a valid Input")