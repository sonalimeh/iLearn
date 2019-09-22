inp=input("Enter video link ")
from youtube_transcript_api import YouTubeTranscriptApi

b=YouTubeTranscriptApi.get_transcript(inp,languages=['en', 'de'])

#importing the module 
from pytube import YouTube 
'''
#link of the video to be downloaded
word=inp
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
        stream.download('D:/Desktop/HackVIT/video') 
except: 
	print("Some Error!") 
print('Task Completed!')

#Enter the data'''


import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
    p=r.recognize_google(audio)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


from rake_nltk import Rake

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()

text=p
# Extraction given the text.
r.extract_keywords_from_text(text)


# Extraction given the list of strings where each string is a sentence.
#r.extract_keywords_from_sentences(<list of sentences>)

# To get keyword phrases ranked highest to lowest.
impword=(r.get_ranked_phrases())
if(impword[0].find('understand')!=-1):
    
    impword[0]=impword[0][11:]
impw=impword[0]
print(impword)
print(impw)
                   


mainword=impw



'''#STOP WORDS
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import nltk
#nltk.download('punkt')

stop_words = {'in','to'}

for i in b:
    #print(i['text'])
    example_sent=i['text']
    word_tokens = word_tokenize(example_sent)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = [] 
  
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w)
            i['text']=''.join(w)'''
#print(b)
final_list=list()
for kk in b:
    print(kk['text'])
    if((kk['text']).find(mainword)!=-1):
        print(kk['start'])
        final_list.append(kk['start'])
    m=kk['start']
print(final_list)
yaxis=list()
for p in range(0,len(final_list)):
               yaxis.append(p)
if(len(final_list)>3):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    df = pd.DataFrame({
        'x': final_list,
        'y': yaxis
    })


    np.random.seed(200)
    k = 3
    #centroids[i] = [x, y]
    centroids = {
        i+1: [np.random.randint(0, max(final_list)), np.random.randint(0, max(yaxis))]
        for i in range(k)
    }
        
    fig = plt.figure(figsize=(5, 5))
    plt.scatter(final_list, yaxis, color='k')
    colmap = {1: 'r', 2: 'g', 3: 'b'}
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colmap[i])
    plt.xlim(0, max(final_list))
    plt.ylim(0, max(yaxis))
    plt.show()


import os

path = 'D:\\Desktop\\HackVIT\\video\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.mp4' in file:
            files.append(os.path.join(r, file))

for f in range(0,len(files)):
    z=files[0]

import imageio
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip(z, final_list[0], m, targetname="test.mp4")

