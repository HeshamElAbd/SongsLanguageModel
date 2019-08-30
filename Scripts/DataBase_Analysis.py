#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:10:42 2019

@author: Hesham El Abd
@Description: Navigating the Song-lyric database
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
