#importing the module 
from pytube import YouTube 

#link of the video to be downloaded
word='2spTnAiQg4M'
link='https://www.youtube.com/watch?v='+word

try: 
	#object creation using YouTube which was imported in the beginning 
	yt = YouTube(link) 
except: 
	print("Connection Error") #to handle exception 
 
stream = yt.streams.first()
stream.download() 
try: 
	#downloading the video
        stream.download('D:/Desktop/HackVIT/') 
except: 
	print("Some Error!") 
print('Task Completed!') 
