#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:10:42 2019

@author: Hesham El Abd
@Description: Extract the song lyrics from the SongLyric dataBase
@DataSource: https://www.kaggle.com/mousehead/songlyrics
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
import string 
## Navigating the database:
data=pd.read_csv("Data/songlyrics/songdata.csv")
print("Number of Artist: "+str(len(set(data.artist))))
unique_words=set()
for song in data.text.to_list():
    for word in song.split(" "):
        word.strip("\n")
        word.strip(".")
        word.strip("?")
        unique_words.add(word.lower())
print("Number of words in the database: "+str(len(unique_words)))
# Average song length:
songLength=[]
for song in data.text.to_list():
    songLength.append(len(song))

songLength=np.array(songLength)
#plot the results
plt.hist(songLength)
plt.xlabel("Number of Words")
plt.ylabel("Counts")
plt.title("Average song length")
plt.show()
########
#Prepearing the first database: 
goodInputSong=True
acceptableChars=string.ascii_lowercase +string.ascii_uppercase+string.punctuation 
songCorpa=""
songIndex=0
for song in data.text.to_list():
    goodInputSong=True
    for words in song:
        for char in words:
            if (char not in acceptableChars):
                goodInputSong=False
        break;
    if goodInputSong:
        songCorpa+=song+"$"
    songIndex+=1
    print("songs Processed: "+str(songIndex))
##############################
# save the DataBase 
with open("DataBase_one.pickle","wb") as output_:
    pickle.dump(songCorpa,output_)










