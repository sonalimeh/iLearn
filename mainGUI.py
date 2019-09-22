import sys
import os
from tkinter import font
import speech_recognition as sr
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import mainGUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    mainGUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    mainGUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


def upload():
    inp="2spTnAiQg4M"
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
    from os import startfile
    startfile('D:/Desktop/HackVIT/video/How To Multiply Matrices - Quick & Easy!.mp4')

def speech():
    

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

    inp="2spTnAiQg4M"
    from youtube_transcript_api import YouTubeTranscriptApi

    b=YouTubeTranscriptApi.get_transcript(inp,languages=['en', 'de'])

    #importing the module 
    from pytube import YouTube

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
    k=mainword+'.mp4'
    import imageio
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    ffmpeg_extract_subclip(z, final_list[0], m, targetname=k)
    from os import startfile
    startfile(k)
    




class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#0a0a0a'#d9d9d9 # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#0a0a0a' # X11 color: 'gray85'
        _ana1color = '#0a0a0a' # X11 color: 'gray85'
        _ana2color = '#0a0a0a' # X11 color: 'gray85'
        font12 = "-family {Limelight} -size 32 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font13 = "-family {Comic Sans MS} -size 11 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 7 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font18 = "-family {Palatino Linotype} -size 10 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font19 = "-family {Palatino Linotype} -size 11 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font21 = "-family {Permanent Marker} -size 11 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font22 = "-family {Segoe UI Black} -size 14 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("1135x778+354+150")
        top.title("__iLearn__")
        top.configure(background="#0a0a0a")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.15, rely=0.059, height=66, width=842)
        self.Label1.configure(background="#0a0a0a")#8c001c
        self.Label1.configure(disabledforeground="#0a0a0a")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#e3dee3")
        self.Label1.configure(text='''__iLearn__''')
        self.Label1.configure(width=842)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.338, rely=0.029, height=106, width=92)
        self.Label2.configure(background="#0a0a0a")
        self.Label2.configure(disabledforeground="#0a0a0a")
        self.Label2.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="./logo.png")
        self.Label2.configure(image=self._img1)
        self.Label2.configure(text='''Label''')
        self.Label2.configure(width=100)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.22, rely=0.45, relheight=0.418, relwidth=0.251)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#0a0a0a")
        self.Frame1.configure(width=285)

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.105, rely=0.031, relheight=0.462
                , relwidth=0.793)
        self.Message1.configure(background="#0a0a0a")
        self.Message1.configure(font=font19)
        self.Message1.configure(foreground="#faccff")
        self.Message1.configure(highlightbackground="#0a0a0a")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Click to upload the video to our NLP model ''')
        self.Message1.configure(width=226)

       
        def uploadd():
            upload()

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.092, rely=0.762, height=53, width=226)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#0a0a0a")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font21)
        self.Button1.configure(foreground="#faccff")
        self.Button1.configure(highlightbackground="#0a0a0a")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Upload''')
        self.Button1.configure(width=226)
        self.Button1.config(command=uploadd)

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.511, rely=0.45, relheight=0.418, relwidth=0.251)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#0a0a0a")
        self.Frame2.configure(width=285)

    

        def speechh():
            speech()
        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx=0.092, rely=0.762, height=53, width=226)
        self.Button2.configure(activebackground="#0a0a0a")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#0a0a0a")
        self.Button2.configure(disabledforeground="#f0a3f0")
        self.Button2.configure(font=font21)
        self.Button2.configure(foreground="#f0a3f0")
        self.Button2.configure(highlightbackground="#0a0a0a")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Record''')
        self.Button2.configure(width=226)
        self.Button2.config(command=speechh)


if __name__ == '__main__':
    vp_start_gui()
