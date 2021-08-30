#imports for terminal
import os

#imports tkinter
from tkinter import *

#imports for video to text conversion
import speech_recognition as sr 

import moviepy.editor as mp

#imports for text summarization
import nltk 

from nltk.corpus import stopwords 

from nltk.cluster.util import cosine_distance

import numpy as np

import networkx as nx 

#Initializing GUI 
root = Tk() 
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight())) 
root.title(" Video to summarized text")


def read_article(punctuated):
    article = punctuated.split(". ")
    sentences = []

    for sentence in article:
        
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" ")) 
    
    return sentences


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(punctuated, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Read text anc split it
    sentences =  read_article(punctuated)

    #Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    #  Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    # print("Indexes of top ranked_sentence order are ", ranked_sentence)    

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))

    Output.insert(END, ". ".join(summarize_text) + ".")
    # Step 5 - Offcourse, output the summarize text





def Take_input():

    #Downloading file from youtube
    link = inputtxt.get("1.0", "end-1c")
    line_summr=int(lines_of_summr.get("1.0", "end-1c"))

    #Downloading file from youtube
    os.system(f'youtube-dl -o "%(title)s.%(ext)s" {link}')

    #Getting name of youtube video
    x = os.popen(f'youtube-dl --get-filename -o "%(title)s.%(ext)s" {link}').readlines()

    #Formatting the name
    video_name=x[0].split('.')[0]

    clip = mp.VideoFileClip(f"{video_name}.mp4") 
    clip.audio.write_audiofile(r"converted.wav")
    r = sr.Recognizer()
    audio = sr.AudioFile("converted.wav")
    with audio as source:
        audio_file = r.record(source,offset=4)
        r.adjust_for_ambient_noise(source)
    result = r.recognize_google(audio_file)


    clip.close()

    #Deleting mp4 and wav files
    os.remove(f"{video_name}.mp4")
    os.remove("converted.wav")

    #Punctuating string using a github repo
    a  = os.popen(f'curl -d "text={result}" http://bark.phon.ioc.ee/punctuator').readlines()

    # Non summarized punctuated text
    text=a[0]
    non_summarized_punc.insert(END, text)
    generate_summary(text, line_summr)


l = Label(text = "Enter youtube link",font=("Courier"))

m = Label(text = "Non summarized punctuated text",font=("Courier")) 

n = Label(text = "Summarized text",font=("Courier"))

o = Label(text = "Enters the number of sentences in summarized text",font=("Courier")) 
 
inputtxt = Text(root, height = 2, 
                width = 80, 
                bg = "light yellow",
                font="Courier")

lines_of_summr = Text(root, height = 2, 
                width = 80, 
                bg = "light yellow",
                font="Courier") 

non_summarized_punc= Text(root, height = 15,
            width = 150,  
            bg = "light cyan",
            font="Courier") 

Output = Text(root, height = 15,  
            width = 150,  
            bg = "light cyan",
            font="Courier") 

Display = Button(root, height = 1, 
                width = 20,  
                text ="Show",
                font="Courier",
				borderwidth=4,
                command = lambda:Take_input()) 


# Label for youtube link
l.pack()

# Text field 
inputtxt.pack()

# Number of lines
o.pack()

# Number of lines
lines_of_summr.pack() 

#Button
Display.pack()

# Label for punctuated text
m.pack() 

# Text field for punctuated text
non_summarized_punc.pack()

# Label for Summarized text
n.pack()   

# Text field for Summarized text
Output.pack() 

mainloop()