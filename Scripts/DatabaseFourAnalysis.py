#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:44:42 2019
@author: Hesham El Abd
@Description: Extract the song lyrics from MetroLyrics DataBase 
@DataSource: https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics
"""
import pandas as pd
import pickle
import string
## Loading the DataBase: 
data=pd.read_csv("Data/380000-lyrics-from-metrolyrics/lyrics.csv")
data=data.dropna()
# Clean the database
# save the DataBase 
goodInputSong=True
acceptableChars=string.ascii_lowercase +string.ascii_uppercase+string.punctuation+"\n"
songCorpa=""
songIndex=0
for song in data.lyrics.to_list():
    goodInputSong=True
    for word in song.split(" "):
        for char in word:
            if (char not in acceptableChars):
                goodInputSong=False
                break
    if goodInputSong:
        songCorpa+=song+"$"
    songIndex+=1
    print("songs Processed: "+str(songIndex))

with open("DataBase_Four.pickle","wb") as output_:
    pickle.dump(songCorpa,output_)

    










    

        
    