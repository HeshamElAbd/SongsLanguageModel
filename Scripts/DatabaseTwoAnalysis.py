#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:59:34 2019

@author: Hesham El Abd
@Description: Extract the song lyrics from Billboard 1964-2015 Songs + Lyrics 
@DataSource: https://www.kaggle.com/rakannimer/billboard-lyrics
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
## Navigating the database:
data=pd.read_csv("Data/billboard-1964-2015-songs-lyrics/billboard_lyrics_1964-2015.csv",
                 encoding = "ISO-8859-1")
data=data.dropna()
print("Number of Artist: "+str(len(set(data.Artist))))
unique_words=set()
for song in data.Lyrics.to_list():
    for word in song.split(" "):
        unique_words.add(word.lower())
print("Number of words in the database: "+str(len(unique_words)))
# Average song length:
songLength=[]
for song in data.Lyrics.to_list():
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
songCorpa=""
for song in data.Lyrics.to_list():
    songCorpa+=song+"$"
##############################
# save the DataBase 
with open("DataBase_Two.pickle","wb") as output_:
    pickle.dump(songCorpa,output_)

    









